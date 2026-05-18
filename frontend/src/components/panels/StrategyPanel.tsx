"use client";

import { FileText, PenLine, Route, Target } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Skeleton } from "@/components/ui/skeleton";
import { PanelContainer } from "@/components/layouts/PanelContainer";
import { useStrategy } from "@/hooks/useAnalysis";
import type { AppetiteLevel } from "@/lib/types";

const FIT_COLORS: Record<AppetiteLevel, string> = {
  strong: "bg-emerald-100 text-emerald-800",
  moderate: "bg-amber-100 text-amber-800",
  limited: "bg-red-100 text-red-800",
};

export function StrategyPanel({ accountId }: { accountId: string }) {
  const { data, isLoading, error } = useStrategy(accountId);

  return (
    <div id="submission-plan">
      <PanelContainer title="Submission Plan" icon={Target}>
        {isLoading ? (
          <div className="space-y-3">
            <Skeleton className="h-24 w-full" />
            <Skeleton className="h-20 w-full" />
          </div>
        ) : error ? (
          <p className="text-sm text-destructive">Failed to load strategy.</p>
        ) : data ? (
          <div className="space-y-5">
            <p className="text-sm text-muted-foreground">{data.submission_summary}</p>

            <div className="space-y-3">
              <h4 className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
                Placement Paths
              </h4>
              <ul className="space-y-4">
                {data.target_carriers.map((target, i) => (
                  <li key={i} className="text-sm border rounded-md p-3 space-y-2">
                    <div className="flex items-center gap-2">
                      <span className="font-semibold">Path {i + 1}</span>
                      <span className={`inline-flex px-1.5 py-0.5 rounded text-xs font-medium ${FIT_COLORS[target.appetite_level]}`}>
                        {target.appetite_level} fit
                      </span>
                    </div>
                    <p className="text-muted-foreground">{target.rationale}</p>
                    {target.key_concerns.length > 0 ? (
                      <p className="text-xs text-amber-600">
                        Friction to pre-answer: {target.key_concerns.join(", ")}
                      </p>
                    ) : null}
                  </li>
                ))}
              </ul>
            </div>

            {data.positioning_notes.length > 0 ? (
              <div className="space-y-2">
                <h4 className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
                  Positioning Notes
                </h4>
                {data.positioning_notes.map((note, i) => (
                  <div key={i} className="text-sm">
                    <span className="font-medium">{note.topic}: </span>
                    <span className="text-muted-foreground">{note.framing}</span>
                  </div>
                ))}
              </div>
            ) : null}

            <div id="submission-narrative" className="rounded-md border bg-muted/35 p-3">
              <div className="mb-2 flex items-center gap-2 text-xs font-semibold uppercase tracking-wider text-muted-foreground">
                <PenLine className="h-4 w-4 text-primary" />
                Draft Submission Narrative
              </div>
              <p className="text-sm text-muted-foreground">
                Position the account around verified controls, known coverage friction, and the missing information that
                must be resolved before underwriters see the submission.
              </p>
            </div>

            <div className="grid gap-2 sm:grid-cols-3">
              <Badge variant="outline" className="justify-center gap-1 py-2">
                <FileText className="h-3.5 w-3.5" />
                Producer Brief
              </Badge>
              <Badge variant="outline" className="justify-center gap-1 py-2">
                <Route className="h-3.5 w-3.5" />
                Submission Plan
              </Badge>
              <Badge variant="outline" className="justify-center gap-1 py-2">
                <PenLine className="h-3.5 w-3.5" />
                Narrative Draft
              </Badge>
            </div>
          </div>
        ) : null}
      </PanelContainer>
    </div>
  );
}
