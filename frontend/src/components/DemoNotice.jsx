export default function DemoNotice({ compact = false }) {
  return (
    <aside className={`demo-notice ${compact ? 'demo-notice--compact' : ''}`}>
      <strong>Demo prototype</strong>
      <span>All claim information shown here is synthetic. PFGuide is not an official government service.</span>
    </aside>
  );
}
