"use client";

import { Target } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Skeleton } from "@/components/ui/skeleton";
import { PanelContainer } from "@/components/layouts/PanelContainer";
import { ReasoningBlock } from "@/components/domain/ReasoningBlock";
import { useStrategy } from "@/hooks/useAnalysis";
import type { AppetiteLevel } from "@/lib/types";

const APPETITE_COLORS: Record<AppetiteLevel, string> = {
  preferred: "bg-emerald-100 text-emerald-800",
  standard: "bg-blue-100 text-blue-800",
  moderate: "bg-amber-100 text-amber-800",
  limited: "bg-red-100 text-red-800",
};

export function StrategyPanel({ accountId }: { accountId: string }) {
  const { data, isLoading, error } = useStrategy(accountId);

  return (
    <PanelContainer title="Submission Strategy" icon={Target}>
      {isLoading ? (
        <div className="space-y-3">
          <Skeleton className="h-24 w-full" />
          <Skeleton className="h-20 w-full" />
        </div>
      ) : error ? (
        <p className="text-sm text-destructive">Failed to load strategy.</p>
      ) : data ? (
        <div className="space-y-5">
          {/* Priority order */}
          <div>
            <h4 className="text-xs font-semibold uppercase tracking-wider text-muted-foreground mb-2">
              Submission Order
            </h4>
            <div className="flex flex-wrap gap-1.5">
              {data.submission_priority_order.map((carrier, i) => (
                <Badge key={i} variant="outline" className="text-xs">
                  {i + 1}. {carrier}
                </Badge>
              ))}
            </div>
          </div>

          {/* Targets */}
          <div className="space-y-3">
            <h4 className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
              Carrier Targets
            </h4>
            <ul className="space-y-4">
              {data.targets.map((target, i) => (
                <li key={i} className="text-sm border rounded-md p-3 space-y-2">
                  <div className="flex items-center gap-2">
                    <span className="font-semibold">{target.carrier}</span>
                    <span className={`inline-flex px-1.5 py-0.5 rounded text-xs font-medium ${APPETITE_COLORS[target.appetite_level]}`}>
                      {target.appetite_level}
                    </span>
                  </div>
                  <p className="text-muted-foreground">{target.reasoning}</p>
                  <div className="flex flex-wrap gap-1">
                    {target.key_strengths.map((s, j) => (
                      <Badge key={j} variant="secondary" className="text-xs">
                        {s}
                      </Badge>
                    ))}
                  </div>
                  {target.potential_concerns.length > 0 && (
                    <p className="text-xs text-amber-600">
                      Concerns: {target.potential_concerns.join(", ")}
                    </p>
                  )}
                </li>
              ))}
            </ul>
          </div>

          {/* Positioning */}
          {data.positioning_notes.length > 0 && (
            <div className="space-y-2">
              <h4 className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
                Positioning Notes
              </h4>
              {data.positioning_notes.map((note, i) => (
                <div key={i} className="text-sm">
                  <span className="font-medium">{note.topic}: </span>
                  <span className="text-muted-foreground">{note.positioning}</span>
                </div>
              ))}
            </div>
          )}

          <ReasoningBlock reasoning={data.reasoning} />
        </div>
      ) : null}
    </PanelContainer>
  );
}
