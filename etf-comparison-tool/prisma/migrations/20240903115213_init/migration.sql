-- CreateTable
CREATE TABLE "ETF" (
    "id" SERIAL NOT NULL,
    "name" TEXT NOT NULL,
    "ticker" TEXT NOT NULL,
    "description" TEXT,
    "expenseRatio" DOUBLE PRECISION NOT NULL,

    CONSTRAINT "ETF_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Holding" (
    "id" SERIAL NOT NULL,
    "ticker" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "percentage" DOUBLE PRECISION NOT NULL,
    "etfId" INTEGER NOT NULL,

    CONSTRAINT "Holding_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "Holding" ADD CONSTRAINT "Holding_etfId_fkey" FOREIGN KEY ("etfId") REFERENCES "ETF"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
