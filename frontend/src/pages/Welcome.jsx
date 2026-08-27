import { useState } from 'react';

import DemoNotice from '../components/DemoNotice';
import ErrorState from '../components/ErrorState';
import { api } from '../services/api';

export default function Welcome({ onDemoAccess }) {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  async function startDemo() {
    setIsLoading(true);
    setError(null);

    try {
      const demoUser = await api.demoLogin();
      onDemoAccess(demoUser.application_id);
    } catch (requestError) {
      setError(requestError);
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <section className="welcome-page">
      <p className="eyebrow">PF CLAIM STATUS, MADE CLEAR</p>

      <h1>Confused by your PF claim status?</h1>

      <p className="lead">
        PFGuide turns confusing claim updates into clear answers:
        what happened, why it happened, and what you can do next.
      </p>

      <DemoNotice />

      {error ? (
        <ErrorState
          error={error}
          onRetry={startDemo}
        />
      ) : null}

      <button
        className="button button--primary"
        type="button"
        onClick={startDemo}
        disabled={isLoading}
      >
        {isLoading ? 'Opening demo…' : 'Try the demo'}
      </button>

      <p className="small-print">
        No personal details, account numbers, passwords, OTPs, or
        government credentials are requested.
      </p>
    </section>
  );
}