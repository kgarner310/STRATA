"use client";

import { TrendingUp } from "lucide-react";
import { Skeleton } from "@/components/ui/skeleton";
import { PanelContainer } from "@/components/layouts/PanelContainer";
import { ImpactBadge, SignalTypeBadge } from "@/components/domain/SignalBadge";
import { ReasoningBlock } from "@/components/domain/ReasoningBlock";
import { useMarket } from "@/hooks/useAnalysis";

export function MarketPanel({ accountId }: { accountId: string }) {
  const { data, isLoading, error } = useMarket(accountId);

  return (
    <PanelContainer title="Market Intelligence" icon={TrendingUp} defaultOpen={false}>
      {isLoading ? (
        <div className="space-y-3">
          <Skeleton className="h-24 w-full" />
          <Skeleton className="h-20 w-full" />
        </div>
      ) : error ? (
        <p className="text-sm text-destructive">Failed to load market data.</p>
      ) : data ? (
        <div className="space-y-5">
          {/* Summary */}
          <p className="text-sm text-muted-foreground">{data.market_summary}</p>

          {/* Signals */}
          <div className="space-y-3">
            <h4 className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
              Market Signals
            </h4>
            <ul className="space-y-3">
              {data.signals.map((signal, i) => (
                <li key={i} className="text-sm space-y-1">
                  <div className="flex items-center gap-2 flex-wrap">
                    <span className="font-medium">{signal.title}</span>
                    <SignalTypeBadge type={signal.signal_type} />
                    <ImpactBadge impact={signal.impact} />
                  </div>
                  <p className="text-muted-foreground">{signal.description}</p>
                  <p className="text-xs text-muted-foreground">Source: {signal.source}</p>
                </li>
              ))}
            </ul>
          </div>

          {/* Carrier intel */}
          <div className="space-y-3">
            <h4 className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
              Carrier Intelligence
            </h4>
            <ul className="space-y-3">
              {data.carrier_intel.map((intel, i) => (
                <li key={i} className="text-sm border rounded-md p-3">
                  <span className="font-semibold">{intel.carrier}</span>
                  <p className="text-muted-foreground mt-0.5">{intel.market_position}</p>
                  <ul className="mt-1.5 space-y-0.5">
                    {intel.recent_actions.map((action, j) => (
                      <li key={j} className="text-xs text-muted-foreground pl-3 relative before:content-['\2022'] before:absolute before:left-0">
                        {action}
                      </li>
                    ))}
                  </ul>
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
