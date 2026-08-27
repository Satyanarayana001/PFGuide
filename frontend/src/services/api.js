const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000';

export class ApiError extends Error {
  constructor(message, status) {
    super(message);
    this.status = status;
  }
}

async function request(path, options = {}) {
  let response;
  try {
    response = await fetch(`${API_BASE_URL}${path}`, {
      headers: { 'Content-Type': 'application/json', ...options.headers },
      ...options,
    });
  } catch {
    throw new ApiError('connection', 0);
  }

  if (!response.ok) {
    throw new ApiError('request', response.status);
  }
  return response.json();
}

export const api = {
  demoLogin: () => request('/api/auth/demo-login', { method: 'POST' }),
  getApplication: (applicationId) =>
    request(`/api/applications/${encodeURIComponent(applicationId)}`),
  getExplanation: (applicationId) =>
    request(`/api/applications/${encodeURIComponent(applicationId)}/explanation`),
  getGrievanceDraft: (applicationId) =>
    request(`/api/applications/${encodeURIComponent(applicationId)}/grievance/draft`, {
      method: 'POST',
    }),
  submitGrievance: (draft) =>
    request('/api/grievances', {
      method: 'POST',
      body: JSON.stringify(draft),
    }),
};
