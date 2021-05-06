"""Írjon programot, amely egy labdarúgó bajnokság meccseit képes legenerálni, és ez alapján
egy rangsort kialakítani a csapatok között. A program először kérjen be egy n számot, majd
pedig n darab csapat nevét. Ezt követően pedig random generálja le a csapatok egymás
elleni meccseinek eredményeit (mindenki játsszon mindenkivel elven), amit a pálda
kimenet alapján kiír a program. A program végül készítsen egy eredménytáblát a meccsek
eredményei alapján (lásd példa kimenet). Pontozás: győzelem: 3 pont, döntetlen: 1 pont,
vereség: 0pont. Ha két csapat azonos pontszámmal végez, akkor közöttük a gólkülönbség
(rúgott gólok – kapott gólok) rangsorol."""

import numpy