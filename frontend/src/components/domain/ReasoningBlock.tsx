"use client";

import { Brain } from "lucide-react";

export function ReasoningBlock({ reasoning }: { reasoning: string }) {
  return (
    <div className="mt-4 rounded-md bg-muted/50 p-3 text-sm">
      <div className="flex items-center gap-1.5 mb-1.5 text-xs font-semibold text-muted-foreground uppercase tracking-wider">
        <Brain className="h-3.5 w-3.5" />
        STRATA Reasoning
      </div>
      <p className="text-muted-foreground leading-relaxed">{reasoning}</p>
    </div>
  );
}
