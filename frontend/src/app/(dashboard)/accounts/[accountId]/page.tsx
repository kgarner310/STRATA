"use client";

import { useParams } from "next/navigation";
import { Skeleton } from "@/components/ui/skeleton";
import { AccountHeader } from "@/components/domain/AccountHeader";
import { PanelGrid } from "@/components/layouts/PanelGrid";
import { AnalysisPanel } from "@/components/panels/AnalysisPanel";
import { CoveragePanel } from "@/components/panels/CoveragePanel";
import { StrategyPanel } from "@/components/panels/StrategyPanel";
import { MarketPanel } from "@/components/panels/MarketPanel";
import { useAccount } from "@/hooks/useAccount";

export default function AccountWorkspacePage() {
  const { accountId } = useParams<{ accountId: string }>();
  const { data: account, isLoading, error } = useAccount(accountId);

  if (isLoading) {
    return (
      <div className="space-y-6">
        <Skeleton className="h-20 w-full" />
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {Array.from({ length: 4 }).map((_, i) => (
            <Skeleton key={i} className="h-64" />
          ))}
        </div>
      </div>
    );
  }

  if (error || !account) {
    return <p className="text-sm text-destructive">Account not found.</p>;
  }

  return (
    <div>
      <AccountHeader account={account} />
      <PanelGrid>
        <AnalysisPanel accountId={accountId} />
        <CoveragePanel accountId={accountId} />
        <StrategyPanel accountId={accountId} />
        <MarketPanel accountId={accountId} />
      </PanelGrid>
    </div>
  );
}
