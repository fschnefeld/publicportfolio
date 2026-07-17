import math


def render_model_cascade_chart() -> str:
    """Inline SVG horizontal bar chart showing forecast model cascade usage."""
    models = [
        ("Prophet", 85, "#7B9E87"),
        ("LightGBM", 70, "#8EB0D6"),
        ("ARIMA", 55, "#D6B98E"),
        ("Croston / ETS", 42, "#A89BD6"),
    ]
    bar_max_w = 220
    row_h = 36
    label_w = 110
    pct_w = 36
    total_w = label_w + bar_max_w + pct_w + 16
    total_h = len(models) * row_h + 8

    rows = []
    for i, (name, pct, color) in enumerate(models):
        y = i * row_h + 20
        bar_w = round(bar_max_w * pct / 100)
        dash_total = bar_max_w + 4
        rows.append(
            f'<text x="{label_w - 8}" y="{y}" '
            f'font-family="DM Mono, monospace" font-size="11" '
            f'fill="rgba(232,230,223,0.55)" text-anchor="end" dominant-baseline="middle">'
            f"{name}</text>"
            f'<line x1="{label_w}" y1="{y}" x2="{label_w + bar_max_w}" y2="{y}" '
            f'stroke="rgba(255,255,255,0.06)" stroke-width="8" stroke-linecap="round"/>'
            f'<line class="chart-bar" x1="{label_w}" y1="{y}" '
            f'x2="{label_w + bar_max_w}" y2="{y}" '
            f'stroke="{color}" stroke-width="8" stroke-linecap="round" '
            f'stroke-dasharray="{bar_w} {dash_total}" '
            f'style="animation-delay:{0.1 + i * 0.14:.2f}s;" />'
            f'<text x="{label_w + bar_max_w + 8}" y="{y}" '
            f'font-family="DM Mono, monospace" font-size="10" '
            f'fill="rgba(232,230,223,0.35)" dominant-baseline="middle">'
            f"{pct}%</text>"
        )

    return (
        f'<div style="margin-top:2.5rem;">'
        f'<p style="font-family:\'DM Mono\',monospace;font-size:0.68rem;'
        f'letter-spacing:0.18em;color:#7B9E87;text-transform:uppercase;'
        f'margin-bottom:1.25rem;">Model cascade · champion selection rate</p>'
        f'<svg viewBox="0 0 {total_w} {total_h}" '
        f'width="100%" style="max-width:{total_w}px;overflow:visible;">'
        + "".join(rows)
        + "</svg></div>"
    )


def render_team_donut() -> str:
    """Inline SVG donut chart showing team composition by discipline."""
    segments = [
        ("Data Science", 2, "#7B9E87"),
        ("Analytics Eng", 2, "#8EB0D6"),
    ]
    total = sum(c for _, c, _ in segments)
    cx, cy, r, stroke_w = 54, 54, 40, 14
    circumference = 2 * math.pi * r

    arcs: list[str] = []
    offset = 0.0
    for name, count, color in segments:
        fraction = count / total
        arc_len = fraction * circumference
        gap = circumference - arc_len
        dash_offset = circumference - offset * circumference / total
        arcs.append(
            f'<circle class="donut-arc" cx="{cx}" cy="{cy}" r="{r}" '
            f'fill="none" stroke="{color}" stroke-width="{stroke_w}" '
            f'stroke-dasharray="{arc_len:.2f} {gap:.2f}" '
            f'stroke-dashoffset="{dash_offset:.2f}" '
            f'style="--dash-offset:{dash_offset:.2f};'
            f'animation-delay:{0.1 + 0.2 * len(arcs):.2f}s;" />'
        )
        offset += count

    legend_items = "".join(
        f'<div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.4rem;">'
        f'<span style="width:8px;height:8px;border-radius:50%;background:{color};'
        f'flex-shrink:0;"></span>'
        f'<span style="font-family:\'DM Mono\',monospace;font-size:0.72rem;'
        f'color:rgba(232,230,223,0.55);">{name} · {count}</span>'
        f"</div>"
        for name, count, color in segments
    )

    return (
        f'<div style="display:flex;align-items:center;gap:2.5rem;margin-top:2rem;">'
        f'<svg viewBox="0 0 108 108" width="108" height="108" '
        f'style="transform:rotate(-90deg);flex-shrink:0;">'
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" '
        f'stroke="rgba(255,255,255,0.06)" stroke-width="{stroke_w}" />'
        + "".join(arcs)
        + '</svg>'
        '<div>'
        '<p style="font-family:\'DM Mono\',monospace;font-size:0.68rem;'
        'letter-spacing:0.18em;color:#7B9E87;text-transform:uppercase;'
        'margin-bottom:0.9rem;">My team · 4 in scope</p>'
        + legend_items
        + "</div></div>"
    )
