"use client";

import { ShieldCheck } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Skeleton } from "@/components/ui/skeleton";
import { PanelContainer } from "@/components/layouts/PanelContainer";
import { useCoverage } from "@/hooks/useAnalysis";
import type { GapType } from "@/lib/types";

const GAP_COLORS: Record<GapType, string> = {
  missing: "bg-red-100 text-red-800",
  inadequate_limit: "bg-amber-100 text-amber-800",
  sublimit_concern: "bg-yellow-100 text-yellow-800",
  exclusion_risk: "bg-orange-100 text-orange-800",
};

export function CoveragePanel({ accountId }: { accountId: string }) {
  const { data, isLoading, error } = useCoverage(accountId);

  return (
    <PanelContainer title="Coverage Gaps" icon={ShieldCheck}>
      {isLoading ? (
        <div className="space-y-3">
          <Skeleton className="h-8 w-24" />
          <Skeleton className="h-24 w-full" />
          <Skeleton className="h-20 w-full" />
        </div>
      ) : error ? (
        <p className="text-sm text-destructive">Failed to load coverage data.</p>
      ) : data ? (
        <div className="space-y-5">
          <div className="flex items-center gap-2">
            <span className="text-sm text-muted-foreground">Submission readiness:</span>
            <span className="text-lg font-bold">{data.adequacy_score}/100</span>
          </div>
          <p className="text-sm text-muted-foreground">{data.summary}</p>

          <div className="space-y-3">
            <h4 className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
              Coverage Friction
            </h4>
            <ul className="space-y-3">
              {data.gaps.map((gap, i) => (
                <li key={i} className="text-sm space-y-1 rounded-md border p-3">
                  <div className="flex items-center gap-2">
                    <span className="font-medium">{gap.line_of_business}</span>
                    <span className={`inline-flex px-1.5 py-0.5 rounded text-xs font-medium ${GAP_COLORS[gap.gap_type]}`}>
                      {gap.gap_type.replaceAll("_", " ")}
                    </span>
                  </div>
                  <p className="text-muted-foreground">{gap.description}</p>
                  <p className="text-xs text-primary">Producer move: {gap.recommendation}</p>
                  {gap.potential_impact ? (
                    <p className="text-xs text-muted-foreground">{gap.potential_impact}</p>
                  ) : null}
                </li>
              ))}
            </ul>
          </div>

          <div className="space-y-3">
            <h4 className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
              Pre-Submission Recommendations
            </h4>
            <ul className="space-y-2">
              {data.recommendations.map((rec, i) => (
                <li key={i} className="text-sm">
                  <span className="font-medium">{rec.line_of_business}</span>
                  <Badge variant="outline" className="ml-2 text-xs">
                    {rec.priority}
                  </Badge>
                  <p className="text-muted-foreground mt-0.5">{rec.rationale}</p>
                </li>
              ))}
            </ul>
          </div>
        </div>
      ) : null}
    </PanelContainer>
  );
}
