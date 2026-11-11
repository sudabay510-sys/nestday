from helpers import L, LM, opt, env_names

Q = [
    {"id": "age", "type": "choice", "prompt": "How old is your little one?",
     "options": [opt("0_3", "0–3 months"), opt("4_6", "4–6 months"), opt("7_12", "7–12 months"), opt("13_24", "13–24 months"), opt("25_36", "2–3 years")]},
    {"id": "red", "type": "choice", "prompt": "Safety check: is any of this happening?",
     "help": "If yes, please contact your pediatrician (or emergency services) before using any schedule.",
     "options": [opt("none", "None of these"), opt("fever", "Fever, trouble breathing, or unusual sleepiness"), opt("feeding", "Poor feeding or fewer wet diapers"), opt("weight", "Concerns about weight gain or growth"), opt("worried", "Something else that worries me")]},
    {"id": "naps", "type": "choice", "prompt": "How many naps most days?",
     "options": [opt("4", "4 or more / unpredictable"), opt("3", "3"), opt("2", "2"), opt("1", "1"), opt("0", "Dropping naps")]},
    {"id": "wake", "type": "choice", "prompt": "Usual morning wake-up time?",
     "options": [opt("6", "Around 6 am"), opt("7", "Around 7 am"), opt("8", "Around 8 am"), opt("var", "It varies a lot")]},
    {"id": "feeding", "type": "choice", "prompt": "Feeding (just so the day blocks fit)?",
     "options": [opt("breast", "Breast / chest feeding"), opt("bottle", "Bottle"), opt("both", "A mix"), opt("solids", "Solids + milk")]},
    {"id": "goal", "type": "choice", "prompt": "What would help most?",
     "options": [opt("rhythm", "A predictable daily rhythm"), opt("bedtime", "A calmer bedtime routine"), opt("naps", "Smoother naps"), opt("share", "Sharing the load with a partner/caregiver")]},
    {"id": "style", "type": "choice", "prompt": "What approach feels right to you?",
     "options": [opt("gentle", "Gentle and responsive"), opt("flexible", "Flexible — follow baby’s cues"), opt("structured", "More structured timing"), opt("unsure", "Not sure yet")]},
    {"id": "care", "type": "choice", "prompt": "Who handles days?",
     "options": [opt("home", "A parent at home"), opt("daycare", "Daycare / nanny on weekdays"), opt("shift", "We trade shifts"), opt("solo", "Solo parenting")]},
    {"id": "sleep_space", "type": "choice", "prompt": "Where does baby sleep at night?",
     "options": [opt("crib", "Own crib / bassinet"), opt("room", "Crib in our room"), opt("bed", "Our bed"), opt("varies", "It varies")]},
]

DAYS = {
    "0_3": ["Newborn days don’t follow clocks — feed on cue and rest when you can.", "Short awake windows; watch for sleepy cues (yawning, looking away).", "Day: light & normal sounds. Night: dim and quiet."],
    "4_6": ["Many babies this age nap 3–4 times; follow cues more than the clock.", "Start a short, repeatable bedtime routine (bath or wipe-down, feed, song, bed).", "Offer naps in a consistent spot when practical."],
    "7_12": ["Many babies move toward 2 naps; transitions can be bumpy.", "Anchor the day with a consistent wake time.", "Keep bedtime routine 20–30 minutes and the same order."],
    "13_24": ["Many toddlers move to 1 nap somewhere in this range.", "Offer choices inside the bedtime routine (which book, which pajamas).", "Keep screens out of the last hour before bed."],
    "25_36": ["Nap needs vary widely; quiet time can replace a dropped nap.", "Use a simple picture chart for the bedtime routine.", "Keep wake-up time steady, even on weekends."],
}


def plan(a):
    age = a.get("age", "4_6")
    red = a.get("red") not in (None, "none")
    sleep_note = "Safe-sleep basics recommended by the American Academy of Pediatrics include placing babies on their back, on a firm flat surface, in their own sleep space without pillows, bumpers, or loose bedding. Talk with your pediatrician about your family’s sleep setup."
    pre = [{"title": "Please call your pediatrician first", "bullets": ["You flagged something that a doctor should hear about. Call your pediatrician’s office or nurse line today.", "If your baby is having trouble breathing, is hard to wake, or you feel it’s an emergency, call 911 (or your local emergency number).", "Come back to the routine ideas once your child has been checked."]}] if red else []
    return {
        "title": f"Nestday rhythm ideas — {L(Q[0]['options'], age)}",
        "summary": f"Goal: {L(Q[5]['options'], a.get('goal')).lower()}. Approach: {L(Q[6]['options'], a.get('style')).lower()}. Days: {L(Q[7]['options'], a.get('care')).lower()}. This is general parenting-routine education — not medical advice, and it doesn’t replace your pediatrician. Every child is different.",
        "preview_sections": pre + [
            {"title": "Day-rhythm ideas for this age (unlocked)", "bullets": DAYS.get(age, DAYS["4_6"])},
            {"title": "Wind-down checklist", "bullets": ["Same order every night (e.g. bath/wipe-down → pajamas → feed → book/song → bed).", "Dim lights 20–30 minutes before bed.", "Keep it short enough that tired caregivers can repeat it."]},
            {"title": "Safe sleep reminder", "body": sleep_note},
        ],
        "locked_sections": [
            {"title": "Sample day blocks", "teaser": "Flexible example days built around your wake time — adjust to your child’s cues."},
            {"title": "Caregiver hand-off sheet", "teaser": "A one-page routine for partners, grandparents, or daycare."},
            {"title": "Age-transition modules", "teaser": "General education for nap transitions and common sleep changes."},
            {"title": "Questions for your pediatrician", "teaser": "A list to bring to your next visit."},
        ],
    }


BRAND = {
    "name": "Nestday", "slug": "nestday", "port": 5113,
    "tagline": "Gentle day-rhythm and bedtime-routine ideas for new parents — education, not medical advice.",
    "eyebrow": "For parents of babies & toddlers · education only",
    "hero_title": "A gentle rhythm for your days — and a calmer bedtime.",
    "hero_lede": "Tell Nestday your child’s age, naps, and what would help most. Get age-based rhythm ideas, a wind-down checklist, and a caregiver hand-off sheet. No strict rules, no shame.",
    "cta_primary": "Build our family rhythm", "cta_short": "Start quiz",
    "cta_band_title": "You’re doing better than you think.",
    "cta_band_text": "Flexible ideas that follow your child’s cues — and point you to your pediatrician when it matters.",
    "honesty_line": "General education only. Not medical advice. No sleep-outcome promises.",
    "safety_title": "Health note",
    "safety_note": "Nestday is not medical care. For fever, breathing trouble, feeding or growth worries, or anything that concerns you, contact your pediatrician. In an emergency, call 911.",
    "audience_line": "Tired parents and caregivers of babies and toddlers (0–3) who want a simple, flexible daily scaffold.",
    "personas": [
        {"title": "First-time parent", "text": "Every day feels different; you’d like a loose shape."},
        {"title": "Back-to-work parent", "text": "Daycare drop-off, evenings, and a bedtime that works for everyone."},
        {"title": "Tag-team caregivers", "text": "Partners or grandparents who need the same playbook."},
    ],
    "journey": [
        {"stage": "Survive", "pain": "Days blur together.", "fix": "Age-based rhythm ideas — flexible, not rigid."},
        {"stage": "Wind down", "pain": "Bedtime is a battle.", "fix": "A short, repeatable wind-down checklist."},
        {"stage": "Share the load", "pain": "Only one person knows the routine.", "fix": "A one-page caregiver hand-off sheet."},
        {"stage": "Ask for help", "pain": "Not sure what’s normal.", "fix": "Clear pointers to call your pediatrician."},
    ],
    "how_steps": [
        {"title": "Answer 9 questions", "text": "Age, naps, goals, approach — plus a safety check."},
        {"title": "See your rhythm ideas", "text": "Day ideas, wind-down checklist, and safe-sleep basics."},
        {"title": "Join the founding list", "text": "No charge today — we’ll email when checkout opens."},
    ],
    "features": [
        {"title": "Age-based ideas", "text": "General patterns by age band, cue-first."},
        {"title": "Wind-down checklist", "text": "Same order, every night."},
        {"title": "Caregiver hand-off", "text": "Everyone on the same page."},
        {"title": "Transition modules", "text": "Subscription: education for nap and sleep changes."},
    ],
    "sample_peek": ["Steady morning wake time", "20–30 minute wind-down", "Back to sleep, own space", "Call your pediatrician if…"],
    "trust_points": [
        {"title": "Not medical care", "text": "We never diagnose or tell you to ignore symptoms."},
        {"title": "No cry-it-out mandates", "text": "You choose the approach that fits your family."},
        {"title": "Safe-sleep basics", "text": "Aligned with general AAP safe-sleep guidance."},
    ],
    "faq": [
        {"q": "Will this make my baby sleep through the night?", "a": "We can’t promise that — every child is different. Nestday offers routine ideas, not outcomes."},
        {"q": "Is this a sleep-training program?", "a": "No. Nestday doesn’t prescribe any sleep-training method. Talk with your pediatrician about approaches."},
        {"q": "Can I use it if my baby has a medical condition?", "a": "Please follow your pediatrician’s guidance first; Nestday is general education only."},
    ],
    "pricing": [
        {"id": "4w", "name": "4-week rhythm", "intro": "$9", "period": "first 4 weeks", "renewal": "$12 / 4 weeks", "includes": ["Age-based rhythm ideas", "Wind-down checklist", "Caregiver hand-off sheet"]},
        {"id": "12w", "name": "12-week growing up", "intro": "$24", "period": "first 12 weeks", "renewal": "$29 / 12 weeks", "featured": True, "includes": ["Everything in 4-week", "Age-transition modules", "Pediatrician question lists"]},
    ],
    "disclaimer_short": "General parenting-routine education only. Not medical advice. Contact your pediatrician with any health concern; call 911 in an emergency.",
    "disclaimer_long": "Nestday provides general, non-medical education about daily routines for babies and toddlers. It does not diagnose, treat, or evaluate any medical, developmental, feeding, or sleep condition, does not prescribe sleep-training methods, and does not replace care from a pediatrician or other licensed clinician. Always follow safe-sleep guidance and your pediatrician’s advice. If you think your child may have a medical emergency, call 911 or your local emergency number. No payments are processed on this site.",
    "font_url": "https://fonts.googleapis.com/css2?family=Varela+Round&family=Mulish:wght@400;500;600;700;800&display=swap",
    "fonts": ("Quicksand", "Mulish"),
    "questions": Q, "generate_plan": plan,
    "voice": "Soft, reassuring, never judgmental. Short sentences for tired eyes.",
    "palette": {"Background (moonlight)": "#F4F3FA", "Alt": "#E9E7F5", "Card": "#FFFFFF", "Ink": "#24223A", "Muted": "#605D7A", "Accent (dusk lavender)": "#6D5BD0", "Accent hover": "#5746B5", "Highlight (peach)": "#F6C6A8"},
    "logo_svg": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none"><rect width="64" height="64" rx="24" fill="#6D5BD0"/><path d="M38 16a16 16 0 1 0 10 28A14 14 0 0 1 38 16z" fill="#F4F3FA"/><circle cx="44" cy="22" r="2.5" fill="#F6C6A8"/><circle cx="49" cy="31" r="1.8" fill="#F6C6A8"/></svg>',
    "css_vars": """
  --bg:#F4F3FA;--bg-alt:#E9E7F5;--card:#FFFFFF;--ink:#24223A;--muted:#605D7A;--line:#DDDAEE;
  --accent:#6D5BD0;--accent-2:#5746B5;--on-accent:#FFFFFF;--hi:#F6C6A8;--radius:20px;
  --font-display:'Quicksand', system-ui, sans-serif;--font-body:'Mulish', system-ui, sans-serif;
  --shadow-card:0 20px 44px rgba(109,91,208,.10);--shadow-btn:0 10px 22px rgba(109,91,208,.25);
  --cta-band-bg:#24223A;--cta-band-ink:#F4F3FA;--cta-band-btn:#F6C6A8;--cta-band-btn-ink:#24223A;--tracking:-0.01em;
""",
    "personality": "background:radial-gradient(800px 420px at 85% -5%, #DAD3F7 0%, transparent 60%), radial-gradient(500px 260px at 5% 95%, #FBE2D3 0%, transparent 60%), var(--bg);",
    "extra_css": "h1,h2{font-weight:700}.btn{border-radius:999px}",
    "dos": ["Lead with reassurance and safety.", "Point to the pediatrician and safe-sleep guidance."],
    "donts": ["Diagnose, give dosing/feeding medical advice, or mandate sleep-training methods.", "Promise sleeping through the night or any outcome."],
}
BRAND.update(env_names("nestday"))
