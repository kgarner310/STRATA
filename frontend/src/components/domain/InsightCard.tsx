"use client";

import { Card, CardContent } from "@/components/ui/card";
import type { LucideIcon } from "lucide-react";

interface InsightCardProps {
  icon: LucideIcon;
  label: string;
  value: string | number;
  subtext?: string;
  color?: "default" | "green" | "amber" | "red";
}

const COLOR_MAP = {
  default: "text-primary",
  green: "text-emerald-600",
  amber: "text-amber-600",
  red: "text-red-600",
};

export function InsightCard({
  icon: Icon,
  label,
  value,
  subtext,
  color = "default",
}: InsightCardProps) {
  return (
    <Card>
      <CardContent className="flex items-center gap-3 py-3 px-4">
        <div className={`rounded-md p-2 bg-muted ${COLOR_MAP[color]}`}>
          <Icon className="h-4 w-4" />
        </div>
        <div className="min-w-0">
          <p className="text-xs text-muted-foreground">{label}</p>
          <p className="text-lg font-semibold leading-tight">{value}</p>
          {subtext && <p className="text-xs text-muted-foreground">{subtext}</p>}
        </div>
      </CardContent>
    </Card>
  );
}
