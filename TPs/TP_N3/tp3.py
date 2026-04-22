# ==================================================
# TP N3: الأنظمة الخبيرة - تمثيل المعرفة والاستدلال
# ==================================================

# --------------------------------------------------
# أولاً: تمثيل المعرفة باستخدام القواميس (Dictionary)
# (النقاط 1 و 2 و 5)
# --------------------------------------------------

# 1. تعريف قاعدة المعرفة (Dictionary)
rules_dict = [
    {"if": ["A", "B"], "then": "C"},
    {"if": ["C"], "then": "D"},
    {"if": ["D", "E"], "then": "F"}
]
facts_dict = ["A", "B", "E"] # الحقائق الأولية

# 2. تنفيذ خوارزمية الاستنتاج للأمام (Forward Chaining)
def forward_chaining_dict(facts, rules):
    current_facts = list(facts)
    added = True
    print("\n--- بدء الاستنتاج للأمام (Dictionary) ---")
    while added:
        added = False
        for rule in rules:
            conditions = rule["if"]
            conclusion = rule["then"]
            # إذا كانت الشروط محققة والنتيجة غير موجودة
            if all(c in current_facts for c in conditions) and conclusion not in current_facts:
                print(f"إضافة حقيقة جديدة: {conclusion}")
                current_facts.append(conclusion)
                added = True
    return current_facts

# 5. تنفيذ خوارزمية الاستنتاج للخلف (Backward Chaining)
def backward_chaining_dict(goal, facts, rules):
    # إذا كان الهدف موجوداً في الحقائق
    if goal in facts:
        return True
    
    # البحث عن القواعد التي تعطي هذا الهدف كنتيجة
    for rule in rules:
        if rule["then"] == goal:
            # التحقق عودياً من الشروط
            if all(backward_chaining_dict(cond, facts, rules) for cond in rule["if"]):
                return True
    return False

# --------------------------------------------------
# ثانياً: تمثيل المعرفة باستخدام التوبل (Tuple of Lists)
# (النقاط 3 و 4 و 5)
# --------------------------------------------------

# 3. تعريف قاعدة المعرفة (Tuple of Lists)
# الهيكل: ( ([شروط], نتيجة), ... )
rules_tuple = (
    (["P", "Q"], "R"),
    (["R"], "S"),
    (["S", "T"], "U")
)
facts_tuple = ["P", "Q", "T"]

# 4. تنفيذ خوارزمية الاستنتاج للأمام للهيكل الجديد
def forward_chaining_tuple(facts, rules):
    current_facts = list(facts)
    added = True
    print("\n--- بدء الاستنتاج للأمام (Tuple) ---")
    while added:
        added = False
        for conditions, conclusion in rules:
            if all(c in current_facts for c in conditions) and conclusion not in current_facts:
                print(f"إضافة حقيقة جديدة: {conclusion}")
                current_facts.append(conclusion)
                added = True
    return current_facts

# 5. تنفيذ خوارزمية الاستنتاج للخلف للهيكل الجديد
def backward_chaining_tuple(goal, facts, rules):
    if goal in facts:
        return True
    
    for conditions, conclusion in rules:
        if conclusion == goal:
            if all(backward_chaining_tuple(cond, facts, rules) for cond in conditions):
                return True
    return False

# ==================================================
# البرنامج الرئيسي (Main Execution)
# ==================================================

# تجربة الجزء الأول (Dictionary)
print("=" * 50 + " الجزء الأول: Dictionary " + "=" * 50)
print(f"الحقائق الأولية: {facts_dict}")
final_facts_dict = forward_chaining_dict(facts_dict, rules_dict)
print(f"قاعدة الحقائق النهائية: {final_facts_dict}")

goal_to_test = "F"
proven = backward_chaining_dict(goal_to_test, facts_dict, rules_dict)
print(f"هل تم إثبات الهدف '{goal_to_test}' بالاستنتاج للخلف؟ {proven}")

print("\n" + "=" * 50 + " الجزء الثاني: Tuple " + "=" * 50)
# تجربة الجزء الثاني (Tuple)
print(f"الحقائق الأولية: {facts_tuple}")
final_facts_tuple = forward_chaining_tuple(facts_tuple, rules_tuple)
print(f"قاعدة الحقائق النهائية: {final_facts_tuple}")

goal_to_test_tuple = "U"
proven_tuple = backward_chaining_tuple(goal_to_test_tuple, facts_tuple, rules_tuple)
print(f"هل تم إثبات الهدف '{goal_to_test_tuple}' بالاستنتاج للخلف؟ {proven_tuple}")

print("=" * 100)