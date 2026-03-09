"use client";

import {
  CheckCircle2,
  ClipboardList,
  MessageCircle,
  ShieldAlert,
} from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import type { ParkingLotBriefResponse } from "@/lib/types";

export function ParkingLotBriefCard({ brief }: { brief: ParkingLotBriefResponse }) {
  return (
    <Card className="max-w-2xl mx-auto">
      <CardHeader className="pb-3">
        <CardTitle className="text-lg">
          Parking Lot Brief &mdash; {brief.account_name}
        </CardTitle>
        <p className="text-sm text-muted-foreground">
          {brief.industry}
          {brief.employee_count && ` \u00b7 ${brief.employee_count} employees`}
          {brief.annual_revenue && ` \u00b7 $${(brief.annual_revenue / 1_000_000).toFixed(1)}M revenue`}
        </p>
      </CardHeader>

      <CardContent className="space-y-5">
        {/* Opening */}
        <div className="rounded-md bg-primary/5 p-4">
          <div className="flex items-center gap-2 mb-1.5 text-sm font-semibold">
            <MessageCircle className="h-4 w-4 text-primary" />
            Opening Talking Point
          </div>
          <p className="text-sm leading-relaxed">{brief.opening_talking_point}</p>
        </div>

        <Separator />

        {/* Confirm */}
        <div>
          <div className="flex items-center gap-2 mb-2 text-sm font-semibold">
            <CheckCircle2 className="h-4 w-4 text-emerald-600" />
            Things to Confirm
          </div>
          <ul className="space-y-1.5">
            {brief.things_to_confirm.map((item, i) => (
              <li key={i} className="text-sm pl-6 relative before:content-[''] before:absolute before:left-2 before:top-2 before:h-1.5 before:w-1.5 before:rounded-full before:bg-emerald-500">
                {item}
              </li>
            ))}
          </ul>
        </div>

        <Separator />

        {/* Coverage */}
        <div>
          <div className="flex items-center gap-2 mb-2 text-sm font-semibold">
            <ClipboardList className="h-4 w-4 text-blue-600" />
            Coverage to Discuss
          </div>
          <ul className="space-y-1.5">
            {brief.coverage_to_discuss.map((item, i) => (
              <li key={i} className="text-sm pl-6 relative before:content-[''] before:absolute before:left-2 before:top-2 before:h-1.5 before:w-1.5 before:rounded-full before:bg-blue-500">
                {item}
              </li>
            ))}
          </ul>
        </div>

        <Separator />

        {/* Underwriter Concern */}
        <div className="rounded-md bg-amber-50 border border-amber-200 p-4">
          <div className="flex items-center gap-2 mb-1.5 text-sm font-semibold text-amber-800">
            <ShieldAlert className="h-4 w-4" />
            Underwriter Will Ask About
          </div>
          <p className="text-sm text-amber-900">{brief.underwriter_concern}</p>
        </div>
      </CardContent>
    </Card>
  );
}
