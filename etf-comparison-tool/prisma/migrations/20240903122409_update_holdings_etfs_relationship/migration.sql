/*
  Warnings:

  - You are about to drop the column `etfId` on the `Holding` table. All the data in the column will be lost.

*/
-- DropForeignKey
ALTER TABLE "Holding" DROP CONSTRAINT "Holding_etfId_fkey";

-- AlterTable
ALTER TABLE "Holding" DROP COLUMN "etfId";

-- CreateTable
CREATE TABLE "_ETFHoldings" (
    "A" INTEGER NOT NULL,
    "B" INTEGER NOT NULL
);

-- CreateIndex
CREATE UNIQUE INDEX "_ETFHoldings_AB_unique" ON "_ETFHoldings"("A", "B");

-- CreateIndex
CREATE INDEX "_ETFHoldings_B_index" ON "_ETFHoldings"("B");

-- AddForeignKey
ALTER TABLE "_ETFHoldings" ADD CONSTRAINT "_ETFHoldings_A_fkey" FOREIGN KEY ("A") REFERENCES "ETF"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "_ETFHoldings" ADD CONSTRAINT "_ETFHoldings_B_fkey" FOREIGN KEY ("B") REFERENCES "Holding"("id") ON DELETE CASCADE ON UPDATE CASCADE;
