"use client";

import { AccountIntakeForm } from "@/components/forms/AccountIntakeForm";

export default function NewAccountPage() {
  return (
    <div>
      <div className="mb-6">
        <h1 className="text-2xl font-bold tracking-tight">New Account</h1>
        <p className="text-sm text-muted-foreground mt-1">
          Enter account details to begin analysis
        </p>
      </div>
      <AccountIntakeForm />
    </div>
  );
}
