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

const SIGNAL_COLORS: Record<"low" | "medium" | "high", string> = {
  low: "bg-gray-100 text-gray-800",
  medium: "bg-amber-100 text-amber-800",
  high: "bg-red-100 text-red-800",
};

export function ImpactBadge({ impact }: { impact: "low" | "medium" | "high" }) {
  return (
    <span className={`inline-flex items-center px-2 py-0.5 rounded text-xs font-medium ${SIGNAL_COLORS[impact]}`}>
      {impact}
    </span>
  );
}

const SIGNAL_TYPE_LABELS: Record<SignalType, string> = {
  trend: "Trend",
  alert: "Alert",
  opportunity: "Opportunity",
  risk: "Risk",
};

export function SignalTypeBadge({ type }: { type: SignalType }) {
  return (
    <Badge variant="outline" className="text-xs">
      {SIGNAL_TYPE_LABELS[type]}
    </Badge>
  );
}
