"use client";

import { AlertTriangle } from "lucide-react";
import { SeverityBadge } from "./SignalBadge";
import type { ExposureItem } from "@/lib/types";

export function ExposureList({ exposures }: { exposures: ExposureItem[] }) {
  const sorted = [...exposures].sort((a, b) => {
    const order = { critical: 0, high: 1, medium: 2, low: 3 };
    return order[a.severity] - order[b.severity];
  });

  return (
    <div className="space-y-3">
      <h4 className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
        Exposures
      </h4>
      <ul className="space-y-3">
        {sorted.map((exp, i) => (
          <li key={i} className="flex gap-3 text-sm">
            <AlertTriangle className="h-4 w-4 mt-0.5 shrink-0 text-amber-500" />
            <div className="flex-1 min-w-0">
              <div className="flex items-center gap-2 mb-0.5">
                <span className="font-medium">{exp.type}</span>
                <SeverityBadge severity={exp.severity} />
              </div>
              <p className="text-muted-foreground">{exp.description}</p>
              <p className="text-xs text-muted-foreground mt-0.5">
                Impact: {exp.potential_impact}
              </p>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
