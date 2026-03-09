"use client";

import { cn } from "@/lib/utils";

function scoreColor(score: number) {
  if (score >= 80) return "text-red-600";
  if (score >= 60) return "text-amber-600";
  if (score >= 40) return "text-yellow-500";
  return "text-emerald-600";
}

function scoreLabel(score: number) {
  if (score >= 80) return "Critical";
  if (score >= 60) return "High";
  if (score >= 40) return "Moderate";
  return "Low";
}

export function RiskScoreGauge({ score }: { score: number }) {
  const pct = Math.min(100, Math.max(0, score));

  return (
    <div className="flex items-center gap-3">
      <div className="relative h-16 w-16">
        <svg viewBox="0 0 36 36" className="h-16 w-16 -rotate-90">
          <circle
            cx="18" cy="18" r="15.5"
            fill="none" stroke="currentColor"
            className="text-muted"
            strokeWidth="3"
          />
          <circle
            cx="18" cy="18" r="15.5"
            fill="none" stroke="currentColor"
            className={scoreColor(score)}
            strokeWidth="3"
            strokeDasharray={`${pct} ${100 - pct}`}
            strokeLinecap="round"
          />
        </svg>
        <span className={cn("absolute inset-0 flex items-center justify-center text-lg font-bold", scoreColor(score))}>
          {score}
        </span>
      </div>
      <div>
        <p className="text-sm font-medium">Risk Score</p>
        <p className={cn("text-xs font-semibold", scoreColor(score))}>{scoreLabel(score)}</p>
      </div>
    </div>
  );
}
