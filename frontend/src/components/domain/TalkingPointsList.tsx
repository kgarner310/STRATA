"use client";

import { MessageSquare } from "lucide-react";
import type { TalkingPoint } from "@/lib/types";

export function TalkingPointsList({ points }: { points: TalkingPoint[] }) {
  const sorted = [...points].sort((a, b) => a.priority - b.priority);

  return (
    <div className="space-y-3">
      <h4 className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
        Talking Points
      </h4>
      <ul className="space-y-2">
        {sorted.map((pt, i) => (
          <li key={i} className="flex gap-2 text-sm">
            <MessageSquare className="h-4 w-4 mt-0.5 shrink-0 text-primary" />
            <div>
              <span className="font-medium">{pt.topic}: </span>
              <span className="text-muted-foreground">{pt.point}</span>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
