"use client";

import { Badge } from "@/components/ui/badge";
import type { Severity, SignalType } from "@/lib/types";

const SEVERITY_VARIANTS: Record<Severity, "default" | "secondary" | "destructive" | "outline"> = {
  low: "secondary",
  medium: "outline",
  high: "default",
  critical: "destructive",
};

export function SeverityBadge({ severity }: { severity: Severity }) {
  return <Badge variant={SEVERITY_VARIANTS[severity]}>{severity}</Badge>;
}

const SIGNAL_COLORS: Record<string, string> = {
  positive: "bg-emerald-100 text-emerald-800",
  negative: "bg-red-100 text-red-800",
  neutral: "bg-gray-100 text-gray-800",
};

export function ImpactBadge({ impact }: { impact: "positive" | "negative" | "neutral" }) {
  return (
    <span className={`inline-flex items-center px-2 py-0.5 rounded text-xs font-medium ${SIGNAL_COLORS[impact]}`}>
      {impact}
    </span>
  );
}

const SIGNAL_TYPE_LABELS: Record<SignalType, string> = {
  rate_change: "Rate Change",
  capacity: "Capacity",
  appetite_shift: "Appetite Shift",
  regulatory: "Regulatory",
  trend: "Trend",
};

export function SignalTypeBadge({ type }: { type: SignalType }) {
  return (
    <Badge variant="outline" className="text-xs">
      {SIGNAL_TYPE_LABELS[type]}
    </Badge>
  );
}
