import React from "react";
import { useForm } from "react-hook-form";

interface UserInput {
  entryName: string;
  amount: number;
  entryDate: string;
  type: string;
  notes: string;
  categoryName: string;
}

export default function EntryForm() {
  const { register, handleSubmit } = useForm<UserInput>();

  const onSubmit = (data: UserInput) => {
    console.log(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("entryName")} id="entryName" type="text" />
      <input {...register("amount")} id="amount" type="number" step="0.01" />
      <input {...register("entryDate")} id="entryDate" type="date" />
      <select {...register("type")} id="type">
        <option value="income">Income</option>
        <option value="expense">Expense</option>
      </select>
      <input {...register("notes")} id="notes" type="text" />
      <input {...register("categoryName")} id="categoryName" type="text" />
      <button type="submit">Submit</button>
    </form>
  );
}



