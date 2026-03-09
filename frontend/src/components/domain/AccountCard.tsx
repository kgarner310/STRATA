"use client";

import Link from "next/link";
import { Building2, MapPin } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import type { AccountSummary } from "@/lib/types";

const BUSINESS_LABELS: Record<string, string> = {
  restaurant: "Restaurant",
  landscaping: "Landscaping",
  manufacturing: "Manufacturing",
  apartment_complex: "Apartment Complex",
  other: "Other",
};

export function AccountCard({ account }: { account: AccountSummary }) {
  return (
    <Link href={`/accounts/${account.id}`}>
      <Card className="transition-all hover:shadow-md hover:border-primary/20 cursor-pointer">
        <CardContent className="py-4 px-5">
          <div className="flex items-start justify-between gap-2">
            <div className="min-w-0">
              <h3 className="font-semibold truncate">{account.business_name}</h3>
              <div className="flex items-center gap-3 mt-1 text-sm text-muted-foreground">
                <span className="flex items-center gap-1">
                  <Building2 className="h-3.5 w-3.5" />
                  {BUSINESS_LABELS[account.business_type] || account.business_type}
                </span>
                <span className="flex items-center gap-1">
                  <MapPin className="h-3.5 w-3.5" />
                  {account.city}, {account.state}
                </span>
              </div>
            </div>
            <Badge variant={account.status === "active" ? "default" : "secondary"}>
              {account.status}
            </Badge>
          </div>
        </CardContent>
      </Card>
    </Link>
  );
}
