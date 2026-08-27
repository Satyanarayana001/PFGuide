import { useEffect, useState } from 'react';

import DemoNotice from '../components/DemoNotice';
import ErrorState from '../components/ErrorState';
import LoadingState from '../components/LoadingState';
import { api } from '../services/api';

export default function ClaimExplanation({
  applicationId,
  onBack,
  onPrepareGrievance,
}) {
  const [explanation, setExplanation] = useState(null);
  const [error, setError] = useState(null);

  async function loadExplanation() {
    setError(null);

    try {
      setExplanation(await api.getExplanation(applicationId));
    } catch (requestError) {
      setError(requestError);
    }
  }

  useEffect(() => {
    loadExplanation();
  }, [applicationId]);

  if (error) {
    return (
      <ErrorState
        error={error}
        onRetry={loadExplanation}
      />
    );
  }

  if (!explanation) {
    return (
      <LoadingState label="Preparing a simple explanation…" />
    );
  }

  return (
    <section className="journey-page">
      <DemoNotice compact />

      <p className="eyebrow">CLAIM EXPLAINED</p>

      <h1>Here is what your claim status means</h1>

      <div className="explanation-section">
        <h2>1 · WHAT HAPPENED?</h2>

        <p>{explanation.what_happened}</p>
      </div>

      <div className="explanation-section">
        <h2>2 · WHY DID THIS HAPPEN?</h2>

        <p>{explanation.why}</p>
      </div>

      <div className="explanation-section">
        <h2>3 · WHAT CAN I DO NOW?</h2>

        <ol className="steps-list">
          {explanation.what_now.map((step) => (
            <li key={step}>{step}</li>
          ))}
        </ol>
      </div>

      <div className="journey-callout">
        <h2>Need more help resolving this?</h2>

        <p>
          We'll prepare a grievance draft using your synthetic claim
          details. You can review and edit it before the simulated
          submission.
        </p>

        <button
          className="button button--primary"
          type="button"
          onClick={onPrepareGrievance}
        >
          Prepare a grievance
        </button>
      </div>

      <button
        className="button button--text back-button"
        type="button"
        onClick={onBack}
      >
        ← Back to claim details
      </button>
    </section>
  );
}