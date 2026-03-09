"use client";

import { Search } from "lucide-react";
import { Skeleton } from "@/components/ui/skeleton";
import { PanelContainer } from "@/components/layouts/PanelContainer";
import { ExposureList } from "@/components/domain/ExposureList";
import { RiskScoreGauge } from "@/components/domain/RiskScoreGauge";
import { TalkingPointsList } from "@/components/domain/TalkingPointsList";
import { QuestionsList } from "@/components/domain/QuestionsList";
import { ReasoningBlock } from "@/components/domain/ReasoningBlock";
import { useAnalysis } from "@/hooks/useAnalysis";

export function AnalysisPanel({ accountId }: { accountId: string }) {
  const { data, isLoading, error } = useAnalysis(accountId);

  return (
    <PanelContainer title="Account Analysis" icon={Search}>
      {isLoading ? (
        <div className="space-y-3">
          <Skeleton className="h-16 w-32" />
          <Skeleton className="h-24 w-full" />
          <Skeleton className="h-20 w-full" />
        </div>
      ) : error ? (
        <p className="text-sm text-destructive">Failed to load analysis.</p>
      ) : data ? (
        <div className="space-y-5">
          <RiskScoreGauge score={data.risk_score} />
          <p className="text-sm text-muted-foreground">{data.industry_comparison}</p>
          <ExposureList exposures={data.exposures} />
          <TalkingPointsList points={data.talking_points} />
          <QuestionsList questions={data.key_questions} />
          <ReasoningBlock reasoning={data.reasoning} />
        </div>
      ) : null}
    </PanelContainer>
  );
}
