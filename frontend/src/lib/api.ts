import type {
  AccountIntakeRequest,
  AccountResponse,
  AccountSummary,
  AnalysisResponse,
  CoverageResponse,
  LoginRequest,
  MarketResponse,
  ParkingLotBriefResponse,
  StrategyResponse,
  UserResponse,
} from "@/lib/types";

export class ApiError extends Error {
  status: number;

  constructor(message: string, status: number) {
    super(message);
    this.name = "ApiError";
    this.status = status;
  }
}

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL ?? "";

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}/api/v1${path}`, {
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
      ...init?.headers,
    },
    ...init,
  });

  if (!response.ok) {
    const payload = await response.json().catch(() => null);
    throw new ApiError(payload?.detail ?? "Request failed", response.status);
  }

  return response.json() as Promise<T>;
}

export const api = {
  login: (body: LoginRequest) =>
    request<UserResponse>("/auth/login", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  logout: () => request<{ message: string }>("/auth/logout", { method: "POST" }),
  getMe: () => request<UserResponse>("/auth/me"),
  listAccounts: () => request<AccountSummary[]>("/accounts"),
  getAccount: (id: string) => request<AccountResponse>(`/accounts/${id}`),
  createAccount: (body: AccountIntakeRequest) =>
    request<AccountResponse>("/accounts/intake", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  getAnalysis: (id: string) => request<AnalysisResponse>(`/analysis/${id}`),
  getCoverage: (id: string) => request<CoverageResponse>(`/coverage/gaps/${id}`),
  getStrategy: (id: string) => request<StrategyResponse>(`/strategy/submission/${id}`),
  getMarket: (id: string) => request<MarketResponse>(`/market/intel/${id}`),
  getBrief: (id: string) => request<ParkingLotBriefResponse>(`/brief/parking-lot/${id}`),
};
