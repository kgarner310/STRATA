"use client";

import { useRouter } from "next/navigation";
import { useState, type FormEvent } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { useCreateAccount } from "@/hooks/useAccount";
import type { AccountIntakeRequest, BusinessType } from "@/lib/types";

const BUSINESS_TYPES: { value: BusinessType; label: string }[] = [
  { value: "restaurant", label: "Restaurant" },
  { value: "landscaping", label: "Landscaping" },
  { value: "manufacturing", label: "Manufacturing" },
  { value: "apartment_complex", label: "Apartment Complex" },
  { value: "other", label: "Other" },
];

const US_STATES = [
  "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA",
  "KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ",
  "NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT",
  "VA","WA","WV","WI","WY",
];

export function AccountIntakeForm() {
  const router = useRouter();
  const createAccount = useCreateAccount();
  const [businessType, setBusinessType] = useState<BusinessType>("restaurant");
  const [state, setState] = useState("PA");

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const fd = new FormData(e.currentTarget);

    const data: AccountIntakeRequest = {
      business_name: fd.get("business_name") as string,
      business_type: businessType,
      address: fd.get("address") as string,
      city: fd.get("city") as string,
      state,
      zip_code: fd.get("zip_code") as string,
      annual_revenue: fd.get("annual_revenue") ? Number(fd.get("annual_revenue")) : undefined,
      employee_count: fd.get("employee_count") ? Number(fd.get("employee_count")) : undefined,
      vehicle_count: fd.get("vehicle_count") ? Number(fd.get("vehicle_count")) : undefined,
      years_in_business: fd.get("years_in_business") ? Number(fd.get("years_in_business")) : undefined,
      naics_code: (fd.get("naics_code") as string) || undefined,
      description: (fd.get("description") as string) || undefined,
      additional_notes: (fd.get("additional_notes") as string) || undefined,
    };

    const result = await createAccount.mutateAsync(data);
    router.push(`/accounts/${result.id}`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="max-w-2xl mx-auto space-y-6">
        <Card>
          <CardHeader>
            <CardTitle>Business Information</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="space-y-2">
                <Label htmlFor="business_name">Business Name *</Label>
                <Input id="business_name" name="business_name" required />
              </div>
              <div className="space-y-2">
                <Label>Business Type *</Label>
                <Select value={businessType} onValueChange={(v) => { if (v) setBusinessType(v as BusinessType); }}>
                  <SelectTrigger><SelectValue /></SelectTrigger>
                  <SelectContent>
                    {BUSINESS_TYPES.map((t) => (
                      <SelectItem key={t.value} value={t.value}>{t.label}</SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>
            </div>

            <div className="space-y-2">
              <Label htmlFor="address">Address *</Label>
              <Input id="address" name="address" required />
            </div>

            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
              <div className="space-y-2 col-span-2 md:col-span-1">
                <Label htmlFor="city">City *</Label>
                <Input id="city" name="city" required />
              </div>
              <div className="space-y-2">
                <Label>State *</Label>
                <Select value={state} onValueChange={(v) => { if (v) setState(v); }}>
                  <SelectTrigger><SelectValue /></SelectTrigger>
                  <SelectContent>
                    {US_STATES.map((s) => (
                      <SelectItem key={s} value={s}>{s}</SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>
              <div className="space-y-2">
                <Label htmlFor="zip_code">ZIP *</Label>
                <Input id="zip_code" name="zip_code" required pattern="\d{5}(-\d{4})?" />
              </div>
              <div className="space-y-2">
                <Label htmlFor="naics_code">NAICS Code</Label>
                <Input id="naics_code" name="naics_code" />
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Business Details</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
              <div className="space-y-2">
                <Label htmlFor="annual_revenue">Annual Revenue ($)</Label>
                <Input id="annual_revenue" name="annual_revenue" type="number" min="0" />
              </div>
              <div className="space-y-2">
                <Label htmlFor="employee_count">Employees</Label>
                <Input id="employee_count" name="employee_count" type="number" min="0" />
              </div>
              <div className="space-y-2">
                <Label htmlFor="vehicle_count">Vehicles</Label>
                <Input id="vehicle_count" name="vehicle_count" type="number" min="0" />
              </div>
              <div className="space-y-2">
                <Label htmlFor="years_in_business">Years in Business</Label>
                <Input id="years_in_business" name="years_in_business" type="number" min="0" />
              </div>
            </div>

            <div className="space-y-2">
              <Label htmlFor="description">Business Description</Label>
              <Textarea id="description" name="description" rows={3} />
            </div>

            <div className="space-y-2">
              <Label htmlFor="additional_notes">Additional Notes</Label>
              <Textarea id="additional_notes" name="additional_notes" rows={2} />
            </div>
          </CardContent>
        </Card>

        <div className="flex justify-end gap-3">
          <Button type="button" variant="outline" onClick={() => router.back()}>
            Cancel
          </Button>
          <Button type="submit" disabled={createAccount.isPending}>
            {createAccount.isPending ? "Creating..." : "Create Account"}
          </Button>
        </div>

        {createAccount.error && (
          <p className="text-sm text-destructive text-center">
            {createAccount.error.message}
          </p>
        )}
      </div>
    </form>
  );
}
