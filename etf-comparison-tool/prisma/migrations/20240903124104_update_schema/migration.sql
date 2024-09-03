/*
  Warnings:

  - You are about to drop the column `percentage` on the `Holding` table. All the data in the column will be lost.
  - You are about to drop the `_ETFHoldings` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE "_ETFHoldings" DROP CONSTRAINT "_ETFHoldings_A_fkey";

-- DropForeignKey
ALTER TABLE "_ETFHoldings" DROP CONSTRAINT "_ETFHoldings_B_fkey";

-- AlterTable
ALTER TABLE "Holding" DROP COLUMN "percentage";

-- DropTable
DROP TABLE "_ETFHoldings";

-- CreateTable
CREATE TABLE "ETF_Holding" (
    "id" SERIAL NOT NULL,
    "etfId" INTEGER NOT NULL,
    "holdingId" INTEGER NOT NULL,
    "percentage" DOUBLE PRECISION NOT NULL,

    CONSTRAINT "ETF_Holding_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "ETF_Holding_etfId_holdingId_key" ON "ETF_Holding"("etfId", "holdingId");

-- AddForeignKey
ALTER TABLE "ETF_Holding" ADD CONSTRAINT "ETF_Holding_etfId_fkey" FOREIGN KEY ("etfId") REFERENCES "ETF"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "ETF_Holding" ADD CONSTRAINT "ETF_Holding_holdingId_fkey" FOREIGN KEY ("holdingId") REFERENCES "Holding"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
