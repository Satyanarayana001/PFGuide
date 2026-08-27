import { useEffect, useState } from 'react';

import DemoNotice from '../components/DemoNotice';
import ErrorState from '../components/ErrorState';
import LoadingState from '../components/LoadingState';
import { api } from '../services/api';

export default function GrievanceDraft({
  applicationId,
  onBack,
  onSubmitted,
}) {
  const [draft, setDraft] = useState(null);
  const [error, setError] = useState(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  async function loadDraft() {
    setError(null);

    try {
      setDraft(await api.getGrievanceDraft(applicationId));
    } catch (requestError) {
      setError(requestError);
    }
  }

  async function submitDraft() {
    setIsSubmitting(true);
    setError(null);

    try {
      onSubmitted(await api.submitGrievance(draft));
    } catch (requestError) {
      setError(requestError);
    } finally {
      setIsSubmitting(false);
    }
  }

  useEffect(() => {
    loadDraft();
  }, [applicationId]);

  if (error && !draft) {
    return (
      <ErrorState
        error={error}
        onRetry={loadDraft}
      />
    );
  }

  if (!draft) {
    return (
      <LoadingState label="Preparing your demo grievance draft…" />
    );
  }

  return (
    <section className="journey-page">
      <DemoNotice compact />

      <p className="eyebrow">REVIEW DRAFT</p>

      <h1>Review your grievance before submission</h1>

      <p className="lead lead--small">
        We've prepared this draft using the details of your synthetic
        claim. You can edit it before submitting the demo.
      </p>

      <label className="draft-field">
        <span>Subject</span>

        <input
          value={draft.subject}
          onChange={(event) =>
            setDraft({
              ...draft,
              subject: event.target.value,
            })
          }
        />
      </label>

      <label className="draft-field">
        <span>Message</span>

        <textarea
          rows="7"
          value={draft.message}
          onChange={(event) =>
            setDraft({
              ...draft,
              message: event.target.value,
            })
          }
        />
      </label>

      {error ? (
        <ErrorState
          error={error}
          onRetry={submitDraft}
        />
      ) : null}

      <p className="submission-note">
        <strong>Demo only.</strong> This submission will not contact
        EPFO, any government agency, or any real grievance system.
      </p>

      <div className="button-row">
        <button
          className="button button--primary"
          type="button"
          onClick={submitDraft}
          disabled={isSubmitting}
        >
          {isSubmitting
            ? 'Submitting demo grievance…'
            : 'Submit demo grievance'}
        </button>

        <button
          className="button button--text"
          type="button"
          onClick={onBack}
          disabled={isSubmitting}
        >
          ← Go back
        </button>
      </div>
    </section>
  );
}