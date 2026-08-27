import { useEffect, useState } from 'react';

import DemoNotice from '../components/DemoNotice';
import ErrorState from '../components/ErrorState';
import LoadingState from '../components/LoadingState';
import { api } from '../services/api';

const labels = {
  service_name: 'Service',
  claim_type: 'Claim type',
  current_stage: 'Current stage',
  issue: 'Issue',
  documents_status: 'Documents',
  submitted_date: 'Submitted',
};

const statusSummaries = {
  ACTION_REQUIRED:
    'Your claim needs one more step before it can continue.',

  PROCESSING:
    'Your claim is still moving through the processing workflow.',

  APPROVED:
    'Your claim has completed review and has been approved.',
};

export default function ClaimOverview({
  applicationId,
  onBack,
  onUnderstand,
}) {
  const [application, setApplication] = useState(null);
  const [error, setError] = useState(null);

  async function loadApplication() {
    setError(null);

    try {
      setApplication(await api.getApplication(applicationId));
    } catch (requestError) {
      setError(requestError);
    }
  }

  useEffect(() => {
    loadApplication();
  }, [applicationId]);

  if (error) {
    return (
      <ErrorState
        error={error}
        onRetry={loadApplication}
      />
    );
  }

  if (!application) {
    return (
      <LoadingState label="Loading your synthetic claim…" />
    );
  }

  return (
    <section className="journey-page">
      <DemoNotice compact />

      <p className="eyebrow">YOUR CLAIM</p>

      <h1>{application.service_name}</h1>

      <div
        className={`status-banner status-banner--${application.status.toLowerCase()}`}
      >
        <span>Claim status</span>

        <strong>
          {application.status.replaceAll('_', ' ')}
        </strong>
      </div>

      <p className="status-summary">
        {statusSummaries[application.status] ??
          'Here is the current status of your synthetic claim.'}
      </p>

      <dl className="details-list">
        {Object.entries(labels).map(([key, label]) => (
          <div
            key={key}
            className={
              key === 'issue' &&
              application.status === 'ACTION_REQUIRED'
                ? 'detail--important'
                : ''
            }
          >
            <dt>{label}</dt>

            <dd>{application[key]}</dd>
          </div>
        ))}
      </dl>

      <div className="journey-callout">
        <h2>Want to understand what happened?</h2>

        <p>
          We'll explain this claim status in simple language and
          show you what you can do next.
        </p>

        <button
          className="button button--primary"
          type="button"
          onClick={onUnderstand}
        >
          Understand my claim
        </button>
      </div>

      <button
        className="button button--text back-button"
        type="button"
        onClick={onBack}
      >
        ← Back to demo start
      </button>
    </section>
  );
}