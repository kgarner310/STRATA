"use client";

import { HelpCircle } from "lucide-react";

export function QuestionsList({ questions }: { questions: string[] }) {
  return (
    <div className="space-y-3">
      <h4 className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
        Key Questions
      </h4>
      <ul className="space-y-2">
        {questions.map((q, i) => (
          <li key={i} className="flex gap-2 text-sm">
            <HelpCircle className="h-4 w-4 mt-0.5 shrink-0 text-amber-500" />
            <span>{q}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}
