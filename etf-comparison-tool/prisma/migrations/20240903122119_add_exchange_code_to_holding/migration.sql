/*
  Warnings:

  - Added the required column `exchangeCode` to the `Holding` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "Holding" ADD COLUMN     "exchangeCode" TEXT NOT NULL;
