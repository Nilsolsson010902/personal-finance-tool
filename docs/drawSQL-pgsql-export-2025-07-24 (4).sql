CREATE TABLE "Entry"(
    "e_id" UUID NOT NULL,
    "e_amount" BIGINT NOT NULL,
    "e_date" DATE NOT NULL,
    "e_name" TEXT NOT NULL,
    "type" VARCHAR(255) CHECK
        ("type" IN('')) NOT NULL,
        "notes" TEXT NOT NULL,
        "c_id" UUID NOT NULL,
        "b_id" UUID NOT NULL
);
ALTER TABLE
    "Entry" ADD PRIMARY KEY("e_id");
CREATE TABLE "Category"(
    "c_id" UUID NOT NULL,
    "c_name" TEXT NOT NULL,
    "c_color" TEXT NOT NULL
);
ALTER TABLE
    "Category" ADD PRIMARY KEY("c_id");
CREATE TABLE "Budget"(
    "b_id" UUID NOT NULL,
    "title" TEXT NOT NULL,
    "start_date" DATE NOT NULL,
    "end_date" DATE NOT NULL,
    "total_amount" BIGINT NOT NULL,
    "u_id" UUID NOT NULL
);
ALTER TABLE
    "Budget" ADD PRIMARY KEY("b_id");
CREATE TABLE "User"(
    "u_id" UUID NOT NULL,
    "firstname" TEXT NOT NULL,
    "lastname" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "password_hash" CHAR(255) NOT NULL,
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE
    "User" ADD PRIMARY KEY("u_id");
CREATE TABLE "RecurringEntry"("frequency" TEXT NOT NULL);
ALTER TABLE
    "RecurringEntry" ADD CONSTRAINT "recurringentry_frequency_foreign" FOREIGN KEY("frequency") REFERENCES "Entry"("e_id");
ALTER TABLE
    "Entry" ADD CONSTRAINT "entry_b_id_foreign" FOREIGN KEY("b_id") REFERENCES "Budget"("b_id");
ALTER TABLE
    "Budget" ADD CONSTRAINT "budget_u_id_foreign" FOREIGN KEY("u_id") REFERENCES "User"("u_id");
ALTER TABLE
    "Entry" ADD CONSTRAINT "entry_c_id_foreign" FOREIGN KEY("c_id") REFERENCES "Category"("c_id");