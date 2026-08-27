export default function ErrorState({ error, onRetry }) {
  const isConnectionError = error?.status === 0;
  const message = isConnectionError
    ? 'PFGuide is unable to connect to the demo service right now. Please make sure the backend is running.'
    : 'We could not complete that demo request. Please try again.';

  return (
    <div className="state-panel state-panel--error" role="alert">
      <h2>Something went wrong</h2>
      <p>{message}</p>
      <button className="button button--secondary" type="button" onClick={onRetry}>
        Retry
      </button>
    </div>
  );
}
