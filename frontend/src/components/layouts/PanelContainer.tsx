"use client";

import type { ReactNode } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";
import { useIsMobile } from "@/hooks/useMediaQuery";
import type { LucideIcon } from "lucide-react";

interface PanelContainerProps {
  title: string;
  icon: LucideIcon;
  children: ReactNode;
  defaultOpen?: boolean;
}

export function PanelContainer({
  title,
  icon: Icon,
  children,
  defaultOpen = true,
}: PanelContainerProps) {
  const isMobile = useIsMobile();

  if (isMobile) {
    return (
      <Accordion defaultValue={defaultOpen ? [0] : []}>
        <AccordionItem className="border rounded-lg">
          <AccordionTrigger className="px-4 py-3 hover:no-underline">
            <span className="flex items-center gap-2 font-semibold text-sm">
              <Icon className="h-4 w-4 text-primary" />
              {title}
            </span>
          </AccordionTrigger>
          <AccordionContent className="px-4 pb-4">{children}</AccordionContent>
        </AccordionItem>
      </Accordion>
    );
  }

  return (
    <Card className="flex flex-col">
      <CardHeader className="pb-3">
        <CardTitle className="flex items-center gap-2 text-sm font-semibold">
          <Icon className="h-4 w-4 text-primary" />
          {title}
        </CardTitle>
      </CardHeader>
      <CardContent className="flex-1 overflow-auto">{children}</CardContent>
    </Card>
  );
}
