"use client";

import { AlertTriangle, TrendingUp } from "lucide-react";
import { Skeleton } from "@/components/ui/skeleton";
import { PanelContainer } from "@/components/layouts/PanelContainer";
import { ImpactBadge, SignalTypeBadge } from "@/components/domain/SignalBadge";
import { useMarket } from "@/hooks/useAnalysis";

export function MarketPanel({ accountId }: { accountId: string }) {
  const { data, isLoading, error } = useMarket(accountId);

  return (
    <PanelContainer title="Market Fit & Friction" icon={TrendingUp} defaultOpen={false}>
      {isLoading ? (
        <div className="space-y-3">
          <Skeleton className="h-24 w-full" />
          <Skeleton className="h-20 w-full" />
        </div>
      ) : error ? (
        <p className="text-sm text-destructive">Failed to load market data.</p>
      ) : data ? (
        <div className="space-y-5">
          <p className="text-sm text-muted-foreground">{data.industry_outlook}</p>

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
                    <ImpactBadge impact={signal.relevance} />
                  </div>
                  <p className="text-muted-foreground">{signal.description}</p>
                  {signal.source ? <p className="text-xs text-muted-foreground">Source: {signal.source}</p> : null}
                </li>
              ))}
            </ul>
          </div>

          <div className="space-y-3">
            <h4 className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
              Placement Friction
            </h4>
            <ul className="space-y-3">
              {data.carrier_intel.map((intel, i) => (
                <li key={i} className="text-sm border rounded-md p-3">
                  <span className="flex items-center gap-2 font-semibold">
                    <AlertTriangle className="h-4 w-4 text-amber-600" />
                    Market conversation {i + 1}
                  </span>
                  <p className="text-muted-foreground mt-0.5">{intel.market_position}</p>
                  <p className="mt-1.5 text-xs text-muted-foreground">{intel.appetite_notes}</p>
                  {intel.recent_changes ? <p className="mt-1 text-xs text-muted-foreground">{intel.recent_changes}</p> : null}
                </li>
              ))}
            </ul>
          </div>
        </div>
      ) : null}
    </PanelContainer>
  );
}
