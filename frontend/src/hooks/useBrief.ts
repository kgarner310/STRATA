"use client";

import { useQuery } from "@tanstack/react-query";
import { api } from "@/lib/api";

export function useBrief(accountId: string) {
  return useQuery({
    queryKey: ["brief", accountId],
    queryFn: () => api.getBrief(accountId),
    enabled: !!accountId,
    staleTime: 5 * 60 * 1000,
  });
}
