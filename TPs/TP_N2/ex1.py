# ==================================================
# دالة الأدوات المساعدة (Utils)
# ==================================================
import copy

faits = []

def initDBs():
    del faits[:]
    print("تم تهيئة قاعدة الحقائق.")

# ==================================================
# حلول التمارين (Logic)
# ==================================================

def afficher_faits():
    """1. عرض قاعدة الحقائق"""
    print(f"الحقائق الموجودة: {faits}")

def ajouter_fait(fait):
    """2. إضافة حقيقة جديدة"""
    if fait not in faits:
        faits.append(fait)
        return True
    return False

# ==================================================
# البرنامج الرئيسي (Main Execution)
# ==================================================
print("\n" + "=" * 20 + " TP N2 Ex1 " + "=" * 20)
initDBs()
ajouter_fait("animal a des plumes")
ajouter_fait("animal a un long cou")
afficher_faits()
print("=" * 50)