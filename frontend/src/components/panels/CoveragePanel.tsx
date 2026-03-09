"use client";

import { ShieldCheck } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Skeleton } from "@/components/ui/skeleton";
import { PanelContainer } from "@/components/layouts/PanelContainer";
import { ReasoningBlock } from "@/components/domain/ReasoningBlock";
import { useCoverage } from "@/hooks/useAnalysis";
import type { GapType } from "@/lib/types";

const GAP_COLORS: Record<GapType, string> = {
  missing: "bg-red-100 text-red-800",
  inadequate: "bg-amber-100 text-amber-800",
  sublimit: "bg-yellow-100 text-yellow-800",
  exclusion: "bg-orange-100 text-orange-800",
};

export function CoveragePanel({ accountId }: { accountId: string }) {
  const { data, isLoading, error } = useCoverage(accountId);

  return (
    <PanelContainer title="Coverage Reasoning" icon={ShieldCheck}>
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
          {/* Coverage score */}
          <div className="flex items-center gap-2">
            <span className="text-sm text-muted-foreground">Coverage Score:</span>
            <span className="text-lg font-bold">{data.current_coverage_score}/100</span>
          </div>

          {/* Gaps */}
          <div className="space-y-3">
            <h4 className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
              Coverage Gaps
            </h4>
            <ul className="space-y-3">
              {[...data.gaps]
                .sort((a, b) => a.priority - b.priority)
                .map((gap, i) => (
                  <li key={i} className="text-sm space-y-1">
                    <div className="flex items-center gap-2">
                      <span className="font-medium">{gap.coverage_line}</span>
                      <span className={`inline-flex px-1.5 py-0.5 rounded text-xs font-medium ${GAP_COLORS[gap.gap_type]}`}>
                        {gap.gap_type}
                      </span>
                    </div>
                    <p className="text-muted-foreground">{gap.description}</p>
                    <p className="text-xs text-primary">
                      Rec: {gap.recommendation}
                    </p>
                  </li>
                ))}
            </ul>
          </div>

          {/* Recommendations */}
          <div className="space-y-3">
            <h4 className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
              Recommendations
            </h4>
            <ul className="space-y-2">
              {data.recommendations.map((rec, i) => (
                <li key={i} className="text-sm">
                  <span className="font-medium">{rec.coverage_type}</span>
                  <Badge variant="outline" className="ml-2 text-xs">{rec.recommended_limit}</Badge>
                  <p className="text-muted-foreground mt-0.5">{rec.rationale}</p>
                </li>
              ))}
            </ul>
          </div>

          <ReasoningBlock reasoning={data.reasoning} />
        </div>
      ) : null}
    </PanelContainer>
  );
}
