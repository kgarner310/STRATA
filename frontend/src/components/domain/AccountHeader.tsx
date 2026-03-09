"use client";

import Link from "next/link";
import { ArrowLeft, Building2, Clock, MapPin } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { buttonVariants } from "@/components/ui/button";
import type { AccountResponse } from "@/lib/types";
import { cn } from "@/lib/utils";

const BUSINESS_LABELS: Record<string, string> = {
  restaurant: "Restaurant",
  landscaping: "Landscaping",
  manufacturing: "Manufacturing",
  apartment_complex: "Apartment Complex",
  other: "Other",
};

export function AccountHeader({ account }: { account: AccountResponse }) {
  return (
    <div className="mb-6 space-y-3">
      <div className="flex items-center gap-2">
        <Link href="/accounts" className={cn(buttonVariants({ variant: "ghost", size: "icon" }))}>
          <ArrowLeft className="h-4 w-4" />
        </Link>
        <div className="flex-1 min-w-0">
          <h1 className="text-xl md:text-2xl font-bold tracking-tight truncate">
            {account.business_name}
          </h1>
          <div className="flex flex-wrap items-center gap-x-4 gap-y-1 text-sm text-muted-foreground mt-1">
            <span className="flex items-center gap-1">
              <Building2 className="h-3.5 w-3.5" />
              {BUSINESS_LABELS[account.business_type] || account.business_type}
            </span>
            <span className="flex items-center gap-1">
              <MapPin className="h-3.5 w-3.5" />
              {account.city}, {account.state}
            </span>
            {account.years_in_business && (
              <span className="flex items-center gap-1">
                <Clock className="h-3.5 w-3.5" />
                {account.years_in_business} yrs
              </span>
            )}
          </div>
        </div>
        <div className="flex items-center gap-2">
          <Link
            href={`/accounts/${account.id}/brief`}
            className={cn(buttonVariants({ variant: "outline", size: "sm" }))}
          >
            Parking Lot Brief
          </Link>
          <Badge variant={account.status === "active" ? "default" : "secondary"}>
            {account.status}
          </Badge>
        </div>
      </div>

      {/* Key metrics */}
      <div className="flex flex-wrap gap-4 text-sm">
        {account.annual_revenue && (
          <div>
            <span className="text-muted-foreground">Revenue: </span>
            <span className="font-medium">
              ${(account.annual_revenue / 1_000_000).toFixed(1)}M
            </span>
          </div>
        )}
        {account.employee_count && (
          <div>
            <span className="text-muted-foreground">Employees: </span>
            <span className="font-medium">{account.employee_count}</span>
          </div>
        )}
        {account.vehicle_count && (
          <div>
            <span className="text-muted-foreground">Vehicles: </span>
            <span className="font-medium">{account.vehicle_count}</span>
          </div>
        )}
      </div>
    </div>
  );
}
