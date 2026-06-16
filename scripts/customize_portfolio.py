from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "screensImages"
PROFILE = Path("/Users/arjhun_03/.gemini/antigravity-ide/brain/e4f55275-5af5-4c81-bc11-046ca35869f7/media__1781549156238.jpg")
W, H = 1344, 888


def font(size, bold=False):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
        str(ROOT / "assets" / "fonts" / "BrownMedium Regular.ttf" if bold else ROOT / "assets" / "fonts" / "BrownLight Regular.ttf"),
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


F = {
    "title": font(46, True),
    "h1": font(38, True),
    "h2": font(28, True),
    "body": font(26),
    "small": font(22),
    "tiny": font(18),
    "folder": font(26, True),
    "icon": font(36, True),
}


def text_size(draw, text, fnt):
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def bg():
    img = Image.new("RGB", (W, H), "#def8c8")
    pix = img.load()
    for y in range(H):
        for x in range(W):
            gx = x / W
            gy = y / H
            r = int(221 + 35 * (1 - abs(gx - 0.55)) * (1 - gy * 0.45))
            g = int(246 - 48 * gx + 18 * gy)
            b = int(199 - 70 * gx + 28 * gy)
            pix[x, y] = (max(190, min(255, r)), max(205, min(255, g)), max(145, min(240, b)))
    d = ImageDraw.Draw(img)
    for x in range(0, W, 56):
        d.line((x, 0, x, H), fill="#ffffff", width=4)
    for y in range(0, H, 50):
        d.line((0, y, W, y), fill="#ffffff", width=4)
    d.rectangle((0, 770, W, H), fill="#ddffd0", outline="#000000", width=6)
    d.rectangle((156, 770, 1175, H), outline="#000000", width=6)
    d.rectangle((1176, 770, W, 832), fill="#ffffff", outline="#000000", width=6)
    d.rectangle((1176, 832, W, H), fill="#ffffff", outline="#000000", width=6)
    d.text((45, 808), "bot", fill="#000000", font=F["small"])
    d.rectangle((1046, 833, 1075, 850), outline="#000000", width=2)
    d.rectangle((1075, 837, 1081, 846), fill="#000000")
    d.rectangle((1050, 837, 1068, 847), fill="#8ce65a")
    for i, h in enumerate([10, 18, 27]):
        d.rectangle((1108 + i * 12, 850 - h, 1115 + i * 12, 850), outline="#000000", width=2, fill="#8ce65a")
    return img


def desktop_icon(d, x, y, label, kind="folder"):
    if kind == "user":
        d.rounded_rectangle((x, y, x + 80, y + 80), radius=10, fill="#fffdf6", outline="#000000", width=5)
        d.ellipse((x + 26, y + 18, x + 54, y + 46), outline="#000000", width=4, fill="#ffe2b7")
        d.arc((x + 18, y + 44, x + 62, y + 82), 190, 350, fill="#000000", width=4)
    elif kind == "note":
        d.rounded_rectangle((x, y, x + 78, y + 78), radius=8, fill="#ffeaa6", outline="#000000", width=5)
        d.line((x + 18, y + 30, x + 58, y + 30), fill="#000000", width=3)
        d.line((x + 18, y + 50, x + 48, y + 50), fill="#000000", width=3)
    elif kind == "doc":
        d.rounded_rectangle((x, y, x + 68, y + 86), radius=5, fill="#ffffff", outline="#000000", width=5)
        d.polygon([(x + 45, y), (x + 68, y + 22), (x + 45, y + 22)], fill="#eeeeee", outline="#000000")
        for off in (36, 50, 64):
            d.line((x + 15, y + off, x + 52, y + off), fill="#000000", width=3)
    elif kind == "trash":
        d.rectangle((x + 18, y + 24, x + 74, y + 100), outline="#000000", width=5, fill="#ffe7b5")
        d.rectangle((x + 8, y + 12, x + 84, y + 28), outline="#000000", width=5, fill="#ffe7b5")
        d.line((x + 30, y + 38, x + 30, y + 86), fill="#000000", width=4)
        d.line((x + 48, y + 38, x + 48, y + 86), fill="#000000", width=4)
        d.line((x + 66, y + 38, x + 66, y + 86), fill="#000000", width=4)
    else:
        d.polygon([(x, y + 24), (x + 28, y + 24), (x + 42, y + 38), (x + 92, y + 38), (x + 92, y + 88), (x, y + 88)], fill="#ffd9a6", outline="#000000")
        d.line((x, y + 24, x, y + 88, x + 92, y + 88, x + 92, y + 38, x + 42, y + 38, x + 28, y + 24, x, y + 24), fill="#000000", width=5)
    tw, _ = text_size(d, label, F["h1"] if len(label) < 12 else F["body"])
    d.text((x + 45 - tw / 2, y + 92), label, fill="#000000", font=F["h1"] if len(label) < 12 else F["body"])


def project_icon(d, x, y, label):
    d.polygon([(x, y + 20), (x + 28, y + 20), (x + 42, y + 34), (x + 94, y + 34), (x + 94, y + 86), (x, y + 86)], fill="#ffd9a6", outline="#000000")
    d.line((x, y + 20, x, y + 86, x + 94, y + 86, x + 94, y + 34, x + 42, y + 34, x + 28, y + 20, x, y + 20), fill="#000000", width=5)
    tw, _ = text_size(d, label, F["folder"])
    d.text((x + 47 - tw / 2, y + 94), label, fill="#000000", font=F["folder"])


def draw_desktop(img):
    d = ImageDraw.Draw(img)
    desktop_icon(d, 76, 60, "User", "user")
    desktop_icon(d, 238, 60, "Notes", "note")
    desktop_icon(d, 78, 236, "Projects", "folder")
    desktop_icon(d, 1028, 62, "credits", "doc")
    desktop_icon(d, 1178, 62, "photos", "folder")
    desktop_icon(d, 1188, 220, "resume.pdf", "doc")
    desktop_icon(d, 1188, 588, "Recycle Bin", "trash")


def window(d, xy, title, color="#e48687"):
    x1, y1, x2, y2 = xy
    d.rectangle(xy, fill="#f8f8ef", outline="#000000", width=4)
    d.rectangle((x1, y1, x2, y1 + 52), fill=color, outline="#000000", width=4)
    d.text((x1 + 28, y1 + 9), title, fill="#000000", font=F["h2"])
    for i, symbol in enumerate(["_", "□", "×"]):
        bx = x2 - 128 + i * 42
        d.rounded_rectangle((bx, y1 + 12, bx + 30, y1 + 42), radius=4, fill="#ffffff", outline="#000000", width=3)
        d.text((bx + 7, y1 + 7), symbol, fill="#000000", font=F["small"])


def wrap_draw(d, text, xy, fnt, fill="#000000", width=46, line_gap=8):
    x, y = xy
    for para in text.split("\n"):
        if not para:
            y += fnt.size
            continue
        for line in textwrap.wrap(para, width=width):
            d.text((x, y), line, fill=fill, font=fnt)
            y += fnt.size + line_gap
    return y


def chips(d, labels, x, y):
    for label in labels:
        tw, th = text_size(d, label, F["small"])
        d.rounded_rectangle((x, y, x + tw + 28, y + 38), radius=8, fill="#ffe3be", outline="#000000", width=3)
        d.text((x + 14, y + 6), label, fill="#000000", font=F["small"])
        x += tw + 42


def paste_profile(img, box):
    x1, y1, x2, y2 = box
    size = (x2 - x1, y2 - y1)
    try:
        src = Image.open(PROFILE).convert("RGB")
    except OSError:
        return
    w, h = src.size
    crop_w = int(w * 0.62)
    crop_h = int(crop_w * size[1] / size[0])
    crop_h = min(crop_h, h)
    crop_x1 = max(0, int(w * 0.24))
    crop_y1 = max(0, int(h * 0.17))
    crop_x2 = min(w, crop_x1 + crop_w)
    crop_y2 = min(h, crop_y1 + crop_h)
    src = src.crop((crop_x1, crop_y1, crop_x2, crop_y2)).resize(size, Image.Resampling.LANCZOS)
    img.paste(src, (x1, y1))


def about():
    img = bg()
    draw_desktop(img)
    d = ImageDraw.Draw(img)
    window(d, (340, 86, 1000, 696), "About User")
    d.rectangle((376, 174, 727, 372), fill="#ffffff", outline="#000000", width=4)
    d.text((405, 238), "Name", fill="#000000", font=F["small"])
    d.text((495, 238), "Arjhun O", fill="#000000", font=F["body"])
    d.text((405, 286), "Role", fill="#000000", font=F["small"])
    d.text((495, 286), "Fullstack Developer", fill="#000000", font=F["small"])
    d.text((405, 334), "Phone", fill="#000000", font=F["small"])
    d.text((495, 334), "8610051714", fill="#000000", font=F["body"])
    d.rectangle((774, 174, 964, 362), fill="#efe0e0", outline="#000000", width=4)
    paste_profile(img, (790, 190, 948, 346))
    d.rectangle((774, 174, 964, 362), outline="#000000", width=4)
    d.rectangle((377, 398, 964, 603), fill="#ffffff", outline="#000000", width=4)
    summary = "Full-stack developer skilled in PHP, MySQL, HTML, CSS, JavaScript and RESTful APIs. I build responsive web apps with clean CRUD flows, database-backed features, and smooth frontend-backend integration."
    wrap_draw(d, summary, (412, 430), F["body"], width=43)
    for i, label in enumerate(["GitHub", "LinkedIn", "Portfolio", "Email"]):
        d.text((388 + i * 110, 625), label, fill="#000000", font=F["small"])
    img.save(OUT / "userScreen.jpg", quality=94)


def projects():
    img = bg()
    draw_desktop(img)
    d = ImageDraw.Draw(img)
    window(d, (128, 170, 980, 682), "")
    d.rectangle((158, 246, 540, 288), fill="#ffffff", outline="#000000", width=4)
    d.text((180, 258), r"C:\User\Documents\Projects", fill="#000000", font=F["small"])
    d.rectangle((158, 310, 950, 654), fill="#ffffff", outline="#000000", width=4)
    labels = ["MinVis", "FinTrack", "El Dorado", "Corpindex", "Code Alpha", "Education", "LeetCode"]
    positions = [(210, 346), (382, 346), (554, 346), (730, 346), (210, 500), (430, 500), (650, 500)]
    for (x, y), label in zip(positions, labels):
        project_icon(d, x, y, label)
    d.rectangle((890, 326, 930, 636), outline="#000000", width=4)
    d.rectangle((894, 434, 926, 556), fill="#86aee4")
    d.text((901, 337), "^", fill="#000000", font=F["h2"])
    d.text((902, 594), "v", fill="#000000", font=F["h2"])
    img.save(OUT / "projectsScreen.jpg", quality=94)


def make_leetcode_thumbnail():
    thumb_dir = ROOT / "assets" / "thumbnails"
    thumb_dir.mkdir(exist_ok=True)
    thumb_path = thumb_dir / "leetcode.png"
    
    img = Image.new("RGB", (564, 310), "#0f0f12")
    d = ImageDraw.Draw(img)
    
    d.text((20, 20), "LeetCode Stats", fill="#ffa116", font=F["title"])
    d.text((20, 80), "Solved: 200+ Problems", fill="#ffffff", font=F["h2"])
    
    categories = [
        ("Easy", "85/100", "#00b8a3", 0.85),
        ("Medium", "102/150", "#ffc01e", 0.68),
        ("Hard", "13/50", "#ef4743", 0.26)
    ]
    
    for i, (cat, val, col, pct) in enumerate(categories):
        y = 135 + i * 55
        d.text((30, y), cat, fill=col, font=F["body"])
        d.text((150, y), val, fill="#ffffff", font=F["body"])
        
        # Draw progress bar
        d.rectangle((270, y + 8, 520, y + 22), fill="#2d2d34")
        d.rectangle((270, y + 8, 270 + int(250 * pct), y + 22), fill=col)
        
    img.save(thumb_path)


def detail(filename, title, subtitle, body, skills, thumb_name, accent="#ffe7c9"):
    img = bg()
    draw_desktop(img)
    d = ImageDraw.Draw(img)
    window(d, (526, 78, 1150, 716), title, accent)
    
    # Paste thumbnail image inside (558, 146, 1122, 456)
    thumb_path = ROOT / "assets" / "thumbnails" / thumb_name
    if thumb_path.exists():
        try:
            thumb_img = Image.open(thumb_path).convert("RGB")
            # Resize thumbnail to exactly 564x310
            thumb_img = thumb_img.resize((564, 310), Image.Resampling.LANCZOS)
            img.paste(thumb_img, (558, 146))
        except Exception as e:
            print(f"Error loading thumbnail {thumb_name}: {e}")
            d.rectangle((558, 146, 1122, 456), fill="#101419", outline="#000000", width=4)
    else:
        d.rectangle((558, 146, 1122, 456), fill="#101419", outline="#000000", width=4)
        
    # Draw double outline around the preview box to fit it in
    d.rectangle((558, 146, 1122, 456), outline="#000000", width=4)
    
    d.rectangle((558, 476, 1122, 692), fill="#ffffff", outline="#000000", width=4)
    # Draw Subtitle at the top of description box
    d.text((584, 492), subtitle, fill="#b15019", font=F["folder"])
    # Draw body description slightly shifted down
    wrap_draw(d, body, (584, 532), F["body"], width=43)
    chips(d, skills, 584, 642)
    img.save(OUT / filename, quality=94)


def notes():
    img = bg()
    draw_desktop(img)
    d = ImageDraw.Draw(img)
    window(d, (270, 110, 1050, 705), "notes", "#ffeaa6")
    d.rectangle((310, 190, 1010, 660), fill="#ffffff", outline="#000000", width=4)
    d.text((350, 224), "Core Stack", fill="#000000", font=F["h1"])
    wrap_draw(d, "PHP, MySQL, JavaScript, HTML, CSS, React.js, Firebase, Tailwind CSS, Recharts, REST APIs, Git, Java, Python", (350, 280), F["body"], width=52)
    d.text((350, 430), "Experience", fill="#000000", font=F["h1"])
    wrap_draw(d, "PHP Developer Intern at Corpindex. Full Stack Intern at Code Alpha. Built APIs, CRUD flows, responsive UI components, and production web features.", (350, 486), F["body"], width=52)
    img.save(OUT / "notesScreen.jpg", quality=94)


def start():
    img = bg()
    draw_desktop(img)
    d = ImageDraw.Draw(img)
    window(d, (300, 145, 1040, 630), "welcome", "#ceffb8")
    d.rectangle((340, 230, 1000, 575), fill="#ffffff", outline="#000000", width=4)
    d.text((382, 270), "ARJHUN O", fill="#000000", font=font(64, True))
    d.text((388, 350), "FULLSTACK DEVELOPER", fill="#000000", font=F["h1"])
    wrap_draw(d, "PHP + MySQL backend, responsive frontend, REST APIs, React/Firebase apps, and practical full-stack product building.", (390, 420), F["body"], width=48)
    img.save(OUT / "startScreen.jpg", quality=94)


def credits():
    img = bg()
    draw_desktop(img)
    d = ImageDraw.Draw(img)
    window(d, (340, 274, 1000, 690), "credits", "#ceffb8")
    d.rectangle((386, 358, 964, 664), fill="#ffffff", outline="#000000", width=4)
    lines = [
        ("Portfolio Owner", "Arjhun O"),
        ("Role", "Fullstack Developer"),
        ("Built From", "Interactive Game Boy 3D portfolio"),
        ("Source Details", "ARJHUN_FULLSTACK_RESUME.pdf"),
    ]
    y = 386
    for heading, value in lines:
        tw, _ = text_size(d, heading, F["h2"])
        d.text((675 - tw / 2, y), heading, fill="#000000", font=F["h2"])
        tw, _ = text_size(d, value, F["body"])
        d.text((675 - tw / 2, y + 34), value, fill="#666666", font=F["body"])
        y += 70
    img.save(OUT / "creditsScreen.jpg", quality=94)


def simple_doc(filename, title, body):
    img = bg()
    draw_desktop(img)
    d = ImageDraw.Draw(img)
    window(d, (330, 120, 1015, 700), title, "#ffffff")
    d.rectangle((370, 198, 975, 650), fill="#ffffff", outline="#000000", width=4)
    wrap_draw(d, body, (410, 238), F["body"], width=48)
    img.save(OUT / filename, quality=94)


def main():
    about()
    projects()
    notes()
    start()
    credits()
    make_leetcode_thumbnail()
    detail(
        "project3DPortfolioScreen.jpg",
        "MinVis",
        "Minimal Intelligent Virtual Interactive System",
        "Full-stack data visualization platform with dynamic frontend-backend interaction and offline AI analysis through Ollama.",
        ["PHP", "MySQL", "JavaScript", "Ollama"],
        "minvis.png"
    )
    detail(
        "projectMobileAppScreen.jpg",
        "FinTrack",
        "Personal Finance Tracker",
        "Real-time income and expense dashboard with transaction history, spending analytics, and Firebase-backed state.",
        ["React.js", "Firebase", "Tailwind", "Recharts"],
        "fintrack.png"
    )
    detail(
        "projectBrowserExtScreen.jpg",
        "El Dorado Casino",
        "Full-Stack Multiplayer Web App",
        "Peer-to-peer multiplayer gaming platform with WebRTC, auth/data sync, immersive UI, and an admin dashboard.",
        ["React 19", "PeerJS", "Supabase", "Zustand"],
        "eldorado.png"
    )
    detail(
        "projectRHGScreen.jpg",
        "Corpindex",
        "PHP Developer Intern",
        "Developed RESTful APIs, optimized app performance, fixed bugs, and shipped full-stack features using PHP and MySQL.",
        ["PHP", "MySQL", "REST APIs", "CRUD"],
        "corpindex.png"
    )
    detail(
        "projectReactPortfolioScreen.jpg",
        "Code Alpha",
        "Full Stack Intern",
        "Built responsive UI components, CRUD functionality, and frontend-backend integrations with web fundamentals.",
        ["HTML", "CSS", "JavaScript", "PHP"],
        "codealpha.png"
    )
    detail(
        "projectFlexboxGameScreen.jpg",
        "Education",
        "B.E. Computer Science Engineering",
        "PSNA College of Engineering and Technology. CGPA 7.8. HSC at StJohn's Metric Higher Secondary School.",
        ["CSE", "CGPA 7.8", "Problem Solving"],
        "education.png"
    )
    detail(
        "projectTicTacToeScreen.jpg",
        "LeetCode",
        "Problem Solver",
        "Solved 200+ problems on LeetCode and enjoy building logic-heavy, user-friendly web applications.",
        ["200+ Problems", "Java", "Python", "DSA"],
        "leetcode.png"
    )
    simple_doc(
        "binDocScreen.jpg",
        "resume.pdf",
        "ARJHUN O\nFULLSTACK DEVELOPER\n\nEmail: arjhun010905@gmail.com\nPhone: 8610051714\nPortfolio: arjhun03.github.io/portfolio\nLinkedIn: arjhun-o-06ab8b334\nLeetCode: arjhun_03",
    )
    simple_doc(
        "binScreen.jpg",
        "recycle bin",
        "Nothing useful was deleted.\n\nYour best work is still on the desktop: MinVis, FinTrack, El Dorado Casino, internships, education, and problem solving.",
    )
    simple_doc(
        "photosScreen.jpg",
        "photos",
        "Project snapshots can go here later.\n\nFor now this folder highlights the portfolio's visual texture system and keeps the original interaction map intact.",
    )
    simple_doc(
        "robotScreen.jpg",
        "assistant",
        "Hi, I am Arjhun's portfolio assistant.\n\nAsk me about PHP, MySQL, REST APIs, responsive UI, React/Firebase dashboards, and full-stack project work.",
    )
    simple_doc("eeveeScreen.jpg", "snapshot", "MinVis\nOffline AI-assisted data analysis with Ollama and dynamic visual dashboards.")
    simple_doc("eeveeScreen2.jpg", "snapshot", "FinTrack\nA modern personal finance tracker with charts, transactions, and real-time backend sync.")
    simple_doc("yoshiScreen.jpg", "snapshot", "El Dorado Casino\nA multiplayer browser game using WebRTC and Supabase.")
    simple_doc("yoshiScreen2.jpg", "snapshot", "Leadership\nEvent coordinator, club president, and collaborative project organizer.")


if __name__ == "__main__":
    main()
