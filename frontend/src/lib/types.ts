export interface UserResponse {
  id: string;
  email: string;
  full_name: string;
  role: "admin" | "producer" | "viewer";
  is_active: boolean;
  created_at: string;
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface PolicyInfo {
  carrier: string;
  line_of_business: string;
  premium?: number | null;
  effective_date?: string | null;
  expiration_date?: string | null;
  limits?: Record<string, unknown>;
  deductibles?: Record<string, unknown>;
}

export type BusinessType = "restaurant" | "landscaping" | "manufacturing" | "apartment_complex" | "other";

export interface AccountIntakeRequest {
  business_name: string;
  business_type: BusinessType;
  naics_code?: string | null;
  address: string;
  city: string;
  state: string;
  zip_code: string;
  annual_revenue?: number | null;
  employee_count?: number | null;
  vehicle_count?: number | null;
  years_in_business?: number | null;
  current_policies?: PolicyInfo[];
  description?: string | null;
  additional_notes?: string | null;
}

export interface AccountSummary {
  id: string;
  business_name: string;
  business_type: string;
  city: string;
  state: string;
  status: string;
  created_at: string;
}

export interface AccountResponse extends AccountSummary {
  naics_code?: string | null;
  address: string;
  zip_code: string;
  annual_revenue?: number | null;
  employee_count?: number | null;
  vehicle_count?: number | null;
  years_in_business?: number | null;
  current_policies: Array<Record<string, unknown>>;
  description?: string | null;
  additional_notes?: string | null;
  created_by: string;
  updated_at: string;
}

export type Severity = "low" | "medium" | "high" | "critical";

export interface ExposureItem {
  type: string;
  severity: Severity;
  description: string;
  mitigation_notes?: string | null;
  potential_impact?: string | null;
}

export interface TalkingPoint {
  topic: string;
  point: string;
  supporting_data?: string | null;
  priority?: number;
}

export interface AnalysisResponse {
  account_id: string;
  risk_score: number;
  key_exposures: ExposureItem[];
  industry_benchmarks: Record<string, unknown>;
  talking_points: TalkingPoint[];
  questions_to_ask: string[];
  computed_at: string;
}

export type GapType = "missing" | "inadequate_limit" | "exclusion_risk" | "sublimit_concern";

export interface CoverageGapItem {
  line_of_business: string;
  gap_type: GapType;
  severity: Severity;
  description: string;
  recommendation: string;
  potential_impact?: string | null;
}

export interface CoverageRecommendation {
  line_of_business: string;
  recommendation: string;
  rationale: string;
  priority: "low" | "medium" | "high";
}

export interface CoverageResponse {
  account_id: string;
  gaps: CoverageGapItem[];
  recommendations: CoverageRecommendation[];
  adequacy_score: number;
  summary: string;
  computed_at: string;
}

export type AppetiteLevel = "strong" | "moderate" | "limited";

export interface SubmissionTarget {
  carrier_name: string;
  appetite_level: AppetiteLevel;
  rationale: string;
  key_concerns: string[];
}

export interface PositioningNote {
  topic: string;
  framing: string;
  supporting_evidence?: string | null;
}

export interface StrategyResponse {
  account_id: string;
  target_carriers: SubmissionTarget[];
  positioning_notes: PositioningNote[];
  submission_summary: string;
  key_differentiators: string[];
  underwriter_concerns: string[];
  computed_at: string;
}

export interface MarketSignal {
  signal_type: "trend" | "alert" | "opportunity" | "risk";
  title: string;
  description: string;
  relevance: "low" | "medium" | "high";
  source?: string | null;
}

export type SignalType = MarketSignal["signal_type"];

export interface CarrierIntel {
  carrier_name: string;
  market_position: string;
  appetite_notes: string;
  recent_changes?: string | null;
}

export interface MarketResponse {
  account_id: string;
  signals: MarketSignal[];
  carrier_intel: CarrierIntel[];
  industry_outlook: string;
  talking_points: string[];
  computed_at: string;
}

export interface ParkingLotBriefResponse {
  account_id: string;
  account_name: string;
  industry: string;
  employee_count?: number | null;
  annual_revenue?: number | null;
  vehicle_count?: number | null;
  things_to_confirm: string[];
  coverage_to_discuss: string;
  underwriter_concern: string;
  opening_talking_point: string;
  risk_score?: number | null;
  computed_at: string;
}
