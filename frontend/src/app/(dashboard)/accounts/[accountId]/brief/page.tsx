"use client";

import { useParams } from "next/navigation";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { buttonVariants } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/skeleton";
import { ParkingLotBriefCard } from "@/components/domain/ParkingLotBriefCard";
import { useBrief } from "@/hooks/useBrief";
import { cn } from "@/lib/utils";

export default function BriefPage() {
  const { accountId } = useParams<{ accountId: string }>();
  const { data: brief, isLoading, error } = useBrief(accountId);

  return (
    <div>
      <div className="flex items-center gap-2 mb-6">
        <Link
          href={`/accounts/${accountId}`}
          className={cn(buttonVariants({ variant: "ghost", size: "icon" }))}
        >
          <ArrowLeft className="h-4 w-4" />
        </Link>
        <div>
          <h1 className="text-xl font-bold tracking-tight">Producer Brief</h1>
          <p className="text-sm text-muted-foreground">
            Pre-call intelligence, questions, and coverage points before you walk in
          </p>
        </div>
      </div>

      {isLoading ? (
        <div className="max-w-2xl mx-auto space-y-4">
          <Skeleton className="h-8 w-48" />
          <Skeleton className="h-24 w-full" />
          <Skeleton className="h-32 w-full" />
          <Skeleton className="h-24 w-full" />
        </div>
      ) : error ? (
        <p className="text-sm text-destructive text-center">Failed to load brief.</p>
      ) : brief ? (
        <ParkingLotBriefCard brief={brief} />
      ) : null}
    </div>
  );
}
