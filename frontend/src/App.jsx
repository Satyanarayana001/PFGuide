import { useState } from 'react';

import Header from './components/Header';
import ClaimExplanation from './pages/ClaimExplanation';
import ClaimOverview from './pages/ClaimOverview';
import GrievanceDraft from './pages/GrievanceDraft';
import Success from './pages/Success';
import Welcome from './pages/Welcome';

const screens = {
  welcome: 'welcome',
  overview: 'overview',
  explanation: 'explanation',
  grievance: 'grievance',
  success: 'success',
};

export default function App() {
  const [screen, setScreen] = useState(screens.welcome);
  const [applicationId, setApplicationId] = useState(null);
  const [submission, setSubmission] = useState(null);

  function beginDemo(applicationIdFromDemo) {
    setApplicationId(applicationIdFromDemo);
    setScreen(screens.overview);
  }

  function restart() {
    setApplicationId(null);
    setSubmission(null);
    setScreen(screens.welcome);
  }

  let content;

  if (screen === screens.overview) {
    content = (
      <ClaimOverview
        applicationId={applicationId}
        onBack={restart}
        onUnderstand={() => setScreen(screens.explanation)}
      />
    );
  } else if (screen === screens.explanation) {
    content = (
      <ClaimExplanation
        applicationId={applicationId}
        onBack={() => setScreen(screens.overview)}
        onPrepareGrievance={() => setScreen(screens.grievance)}
      />
    );
  } else if (screen === screens.grievance) {
    content = (
      <GrievanceDraft
        applicationId={applicationId}
        onBack={() => setScreen(screens.explanation)}
        onSubmitted={(receipt) => {
          setSubmission(receipt);
          setScreen(screens.success);
        }}
      />
    );
  } else if (screen === screens.success) {
    content = (
      <Success
        submission={submission}
        onRestart={restart}
      />
    );
  } else {
    content = <Welcome onDemoAccess={beginDemo} />;
  }

  return (
    <main className="app-shell">
      <Header />

      <div
        className="progress"
        aria-label={`Step ${Object.values(screens).indexOf(screen) + 1} of 5`}
      >
        {Object.values(screens).map((item) => (
          <span
            className={item === screen ? 'progress__active' : ''}
            key={item}
          />
        ))}
      </div>

      {content}
    </main>
  );
}