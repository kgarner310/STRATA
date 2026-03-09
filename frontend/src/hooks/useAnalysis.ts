"use client";

import { useQuery } from "@tanstack/react-query";
import { api } from "@/lib/api";

export function useAnalysis(accountId: string) {
  return useQuery({
    queryKey: ["analysis", accountId],
    queryFn: () => api.getAnalysis(accountId),
    enabled: !!accountId,
    staleTime: 5 * 60 * 1000,
  });
}

export function useCoverage(accountId: string) {
  return useQuery({
    queryKey: ["coverage", accountId],
    queryFn: () => api.getCoverage(accountId),
    enabled: !!accountId,
    staleTime: 5 * 60 * 1000,
  });
}

export function useStrategy(accountId: string) {
  return useQuery({
    queryKey: ["strategy", accountId],
    queryFn: () => api.getStrategy(accountId),
    enabled: !!accountId,
    staleTime: 5 * 60 * 1000,
  });
}

export function useMarket(accountId: string) {
  return useQuery({
    queryKey: ["market", accountId],
    queryFn: () => api.getMarket(accountId),
    enabled: !!accountId,
    staleTime: 5 * 60 * 1000,
  });
}
