"use client";

import type { ReactNode } from "react";

export function PanelGrid({ children }: { children: ReactNode }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-6">
      {children}
    </div>
  );
}
