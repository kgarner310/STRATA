"use client";

import Link from "next/link";
import { Plus } from "lucide-react";
import { buttonVariants } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/skeleton";
import { AccountCard } from "@/components/domain/AccountCard";
import { useAccounts } from "@/hooks/useAccount";
import { cn } from "@/lib/utils";

export default function AccountsPage() {
  const { data: accounts, isLoading, error } = useAccounts();

  return (
    <div>
      <div className="flex items-center justify-between mb-6">
        <div>
          <h1 className="text-2xl font-bold tracking-tight">Accounts</h1>
          <p className="text-sm text-muted-foreground mt-1">
            Select an account to view its workspace
          </p>
        </div>
        <Link href="/accounts/new" className={cn(buttonVariants())}>
          <Plus className="h-4 w-4 mr-2" />
          New Account
        </Link>
      </div>

      {isLoading ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {Array.from({ length: 4 }).map((_, i) => (
            <Skeleton key={i} className="h-20" />
          ))}
        </div>
      ) : error ? (
        <p className="text-sm text-destructive">Failed to load accounts.</p>
      ) : accounts?.length === 0 ? (
        <div className="text-center py-12">
          <p className="text-muted-foreground mb-4">No accounts yet.</p>
          <Link href="/accounts/new" className={cn(buttonVariants())}>
            Create your first account
          </Link>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {accounts?.map((account) => (
            <AccountCard key={account.id} account={account} />
          ))}
        </div>
      )}
    </div>
  );
}
