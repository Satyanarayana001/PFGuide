import DemoNotice from '../components/DemoNotice';

export default function Success({ submission, onRestart }) {
  return (
    <section className="success-page">
      <DemoNotice compact />
      <div className="success-icon" aria-hidden="true">✓</div>
      <p className="eyebrow">DEMO SUBMISSION COMPLETE</p>
      <h1>Your demo grievance was submitted</h1>
      <p>Your synthetic reference number is</p>
      <output className="reference-number">{submission.reference_number}</output>
      <p className="lead lead--small">
        This submission was simulated. No grievance was sent to EPFO or any government system.
      </p>
      <button className="button button--primary" type="button" onClick={onRestart}>
        Start again
      </button>
    </section>
  );
}
