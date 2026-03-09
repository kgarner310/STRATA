"""Pre-computed mock responses for demo accounts.

Each business type has results for all 4 pillars: analysis, coverage, strategy, market.
These power the full demo without requiring any LLM API keys.
"""
from __future__ import annotations

from datetime import datetime, timezone

NOW = datetime.now(timezone.utc).isoformat()

MOCK_ANALYSIS: dict[str, dict] = {
    "restaurant": {
        "risk_score": 68,
        "key_exposures": [
            {
                "type": "fire",
                "severity": "high",
                "description": "Commercial kitchen with deep fryers, gas ranges, and hood suppression system. Fire is the leading cause of restaurant property losses.",
                "mitigation_notes": "Verify Ansul system inspection is current. Check grease trap maintenance schedule.",
            },
            {
                "type": "liquor_liability",
                "severity": "high",
                "description": "Full bar service with wine and cocktails creates dram shop exposure. Pennsylvania has strict liquor liability statutes.",
                "mitigation_notes": "Confirm RAMP certification for all servers. Review incident log for past 12 months.",
            },
            {
                "type": "slip_and_fall",
                "severity": "medium",
                "description": "High foot traffic dining area with kitchen spill potential. Restroom and entryway areas are common claim sources.",
                "mitigation_notes": "Check floor mat placement and non-slip surface coverage in kitchen.",
            },
            {
                "type": "food_contamination",
                "severity": "medium",
                "description": "Italian cuisine with fresh ingredients. Allergen exposure (gluten, dairy, shellfish) and foodborne illness risk.",
                "mitigation_notes": "Review food handling certifications and allergen labeling practices.",
            },
            {
                "type": "workers_comp",
                "severity": "medium",
                "description": "Kitchen burns, cuts, and repetitive motion injuries are common. 28 employees increases frequency exposure.",
                "mitigation_notes": "Review loss runs for workers comp trends over past 3 years.",
            },
        ],
        "industry_benchmarks": {
            "average_gl_premium_per_sqft": 2.85,
            "loss_ratio_industry_avg": 0.58,
            "claim_frequency_per_100_employees": 12.3,
        },
        "talking_points": [
            {
                "topic": "Kitchen Fire Prevention",
                "point": "Restaurants with documented quarterly hood suppression inspections see 40% lower fire claim frequency.",
                "supporting_data": "NFPA 96 compliance data, 2024 restaurant loss analysis",
            },
            {
                "topic": "Liquor Liability Exposure",
                "point": "PA dram shop laws create direct liability for establishments serving visibly intoxicated patrons.",
                "supporting_data": "PA Liquor Code Section 4-497",
            },
            {
                "topic": "Revenue Growth Impact",
                "point": "At $1.8M revenue, this account is above the typical small restaurant threshold. Premium should reflect actual sales, not estimates.",
                "supporting_data": "Industry median restaurant revenue: $1.1M",
            },
        ],
        "questions_to_ask": [
            "When was your Ansul fire suppression system last inspected?",
            "Do you have RAMP certification for all bartenders and servers?",
            "Have you had any liquor-related incidents in the past 3 years?",
            "What is your catering or off-premises event revenue?",
            "Do you have any outdoor dining or patio areas?",
            "What food delivery platforms do you use, and what is that revenue percentage?",
        ],
        "computed_at": NOW,
    },
    "landscaping": {
        "risk_score": 62,
        "key_exposures": [
            {
                "type": "auto_fleet",
                "severity": "high",
                "description": "Multiple trucks and trailers traveling between job sites daily. MVR history and vehicle maintenance are critical.",
                "mitigation_notes": "Pull MVRs for all drivers. Verify DOT compliance if over 10,001 GVWR.",
            },
            {
                "type": "equipment_theft",
                "severity": "high",
                "description": "Mowers, trimmers, and specialty equipment left on trailers overnight at job sites. Inland marine exposure.",
                "mitigation_notes": "GPS tracking on trailers? Locked storage vs. open trailer overnight?",
            },
            {
                "type": "chemical_application",
                "severity": "medium",
                "description": "Pesticide and herbicide application creates pollution liability exposure. Drift to adjacent properties.",
                "mitigation_notes": "Verify applicator licenses are current. Check for pollution liability coverage.",
            },
            {
                "type": "workers_comp",
                "severity": "medium",
                "description": "Heat exposure, equipment injuries, and tree work create significant WC exposure. Class code 0042 is high-hazard.",
                "mitigation_notes": "Any tree removal work? That changes the class code significantly.",
            },
        ],
        "industry_benchmarks": {
            "average_auto_premium_per_vehicle": 3200,
            "inland_marine_rate_per_100_value": 4.5,
            "wc_rate_per_100_payroll": 8.75,
        },
        "talking_points": [
            {
                "topic": "Fleet Safety",
                "point": "Landscaping companies with telematics programs see 25% reduction in auto claims within the first year.",
                "supporting_data": "Insurance Institute fleet safety benchmarks",
            },
            {
                "topic": "Equipment Coverage",
                "point": "Inland marine coverage should include seasonal equipment valuation. Spring inventory values differ significantly from winter.",
                "supporting_data": "Equipment depreciation schedules for commercial landscaping",
            },
        ],
        "questions_to_ask": [
            "Do any of your vehicles exceed 10,001 lbs GVWR?",
            "Do you perform any tree removal or stump grinding?",
            "Where is equipment stored overnight -- secured yard or job site trailers?",
            "Do you apply any pesticides or herbicides? Who holds the applicator license?",
            "Do you subcontract any work? If so, do you collect certificates of insurance?",
            "What is your snow removal revenue in winter months?",
        ],
        "computed_at": NOW,
    },
    "manufacturing": {
        "risk_score": 78,
        "key_exposures": [
            {
                "type": "products_liability",
                "severity": "critical",
                "description": "CNC-machined steel components used in industrial applications. Product failure could cause injury or property damage downstream.",
                "mitigation_notes": "Review quality control documentation. What industries do finished products serve?",
            },
            {
                "type": "equipment_breakdown",
                "severity": "high",
                "description": "CNC machines, hydraulic presses, and welding equipment represent significant capital. Breakdown halts production.",
                "mitigation_notes": "Verify equipment breakdown coverage includes business income for production downtime.",
            },
            {
                "type": "cyber",
                "severity": "high",
                "description": "CNC machines connected to network for CAD/CAM file transfer. Ransomware could halt all production.",
                "mitigation_notes": "Is the CNC network segmented from the business network? Backup procedures?",
            },
            {
                "type": "osha_compliance",
                "severity": "medium",
                "description": "Metal fabrication has specific OSHA requirements for machine guarding, PPE, and noise exposure. 52 employees increases inspection likelihood.",
                "mitigation_notes": "Any OSHA citations in the past 5 years? Review experience modification rate.",
            },
            {
                "type": "environmental",
                "severity": "medium",
                "description": "Metal cutting fluids, welding fumes, and scrap disposal create environmental exposure. Potential soil or groundwater contamination.",
                "mitigation_notes": "Review waste disposal procedures and environmental compliance documentation.",
            },
        ],
        "industry_benchmarks": {
            "average_products_liability_rate": 0.85,
            "equipment_breakdown_frequency": 0.12,
            "cyber_incident_rate_manufacturing": 0.23,
        },
        "talking_points": [
            {
                "topic": "Products Liability",
                "point": "Steel fabrication products used in safety-critical applications require completed operations coverage with adequate limits.",
                "supporting_data": "Manufacturing products liability claim severity trending up 15% annually",
            },
            {
                "topic": "Cyber Risk in Manufacturing",
                "point": "43% of cyberattacks target manufacturing. CNC-connected systems are particularly vulnerable to operational technology attacks.",
                "supporting_data": "IBM X-Force Threat Intelligence Index",
            },
            {
                "topic": "Experience Modification Rate",
                "point": "Current EMR directly impacts workers comp premium. A 1.15 EMR means 15% surcharge on manual premium.",
                "supporting_data": "NCCI experience rating methodology",
            },
        ],
        "questions_to_ask": [
            "What industries are your finished steel components used in?",
            "Are your CNC machines on a separate network from business systems?",
            "What is your current experience modification rate (EMR)?",
            "Do you have any contracts requiring hold-harmless or additional insured status?",
            "What is your annual scrap metal and waste disposal procedure?",
            "Have you had any product recalls or product liability claims?",
        ],
        "computed_at": NOW,
    },
    "apartment_complex": {
        "risk_score": 58,
        "key_exposures": [
            {
                "type": "premises_liability",
                "severity": "high",
                "description": "48 units with common areas, parking, and grounds. Tenant slip-and-fall, stairway falls, and parking lot incidents.",
                "mitigation_notes": "Review maintenance logs for common areas. Lighting adequacy in parking areas.",
            },
            {
                "type": "property_damage",
                "severity": "high",
                "description": "Multi-unit building with shared walls and systems. Water damage from plumbing failures is the #1 property claim for apartments.",
                "mitigation_notes": "Age of plumbing and HVAC systems? Any recent renovations?",
            },
            {
                "type": "habitability",
                "severity": "medium",
                "description": "PA landlord-tenant law requires maintained habitable conditions. Mold, heating failures, and pest issues create legal exposure.",
                "mitigation_notes": "Review any tenant complaints or code violations in past 24 months.",
            },
            {
                "type": "crime_fidelity",
                "severity": "medium",
                "description": "Property management handles security deposits and rent collection. Employee dishonesty exposure for funds management.",
                "mitigation_notes": "Background checks on property management staff? Cash handling procedures?",
            },
        ],
        "industry_benchmarks": {
            "average_property_rate_per_unit": 425,
            "gl_rate_per_unit": 85,
            "water_damage_claim_frequency": 0.18,
        },
        "talking_points": [
            {
                "topic": "Water Damage Prevention",
                "point": "Water damage accounts for 48% of apartment property claims. Automatic shutoff valves can reduce severity by 70%.",
                "supporting_data": "Insurance Institute for Business & Home Safety data",
            },
            {
                "topic": "Tenant Liability",
                "point": "Requiring tenant renters insurance reduces the property owner's subrogation exposure and improves overall loss experience.",
                "supporting_data": "Properties requiring renters insurance see 15% lower GL claims",
            },
        ],
        "questions_to_ask": [
            "What year was the building constructed and when was it last renovated?",
            "Do you require tenants to carry renters insurance?",
            "What is the occupancy rate over the past 12 months?",
            "Are there any swimming pools, playgrounds, or fitness centers on premises?",
            "How many maintenance staff do you have on-site?",
            "Have you had any building code violations or fire marshal citations?",
        ],
        "computed_at": NOW,
    },
}

MOCK_COVERAGE: dict[str, dict] = {
    "restaurant": {
        "gaps": [
            {
                "line_of_business": "Liquor Liability",
                "gap_type": "inadequate_limit",
                "severity": "high",
                "description": "Current $500K liquor liability limit is low for full-bar restaurant in PA. Dram shop claims regularly exceed $1M.",
                "recommendation": "Increase to $1M/$2M or match GL aggregate. Consider excess/umbrella layering.",
                "potential_impact": "Single dram shop judgment could exceed policy limits, exposing business assets.",
            },
            {
                "line_of_business": "Cyber Liability",
                "gap_type": "missing",
                "severity": "medium",
                "description": "No cyber coverage. POS system processes credit cards. PA data breach notification law applies.",
                "recommendation": "Add cyber liability with $500K limit minimum. Include PCI-DSS coverage and breach response.",
                "potential_impact": "POS breach affecting 10,000+ cards could cost $250K-$500K in notification and remediation.",
            },
            {
                "line_of_business": "Employment Practices",
                "gap_type": "missing",
                "severity": "medium",
                "description": "28 employees with no EPLI coverage. Restaurant industry has elevated harassment and discrimination claim frequency.",
                "recommendation": "Add EPLI with $500K limit. Include third-party coverage for customer-employee interactions.",
                "potential_impact": "Average EPLI claim costs $75K to defend, even when unfounded.",
            },
        ],
        "recommendations": [
            {
                "line_of_business": "Umbrella/Excess",
                "recommendation": "Increase umbrella from $1M to $2M to properly layer over GL and liquor liability.",
                "rationale": "At $1.8M revenue with full bar, current umbrella capacity is thin.",
                "priority": "high",
            },
            {
                "line_of_business": "Business Income",
                "recommendation": "Verify business income limit reflects actual 12-month revenue plus extra expense.",
                "rationale": "Many restaurants are underinsured for business interruption. Recovery period often exceeds 6 months.",
                "priority": "medium",
            },
        ],
        "adequacy_score": 62,
        "summary": "Coverage program has significant gaps in liquor liability limits and completely lacks cyber and EPLI protection. The umbrella layer is thin for the exposure profile. Immediate attention needed on liquor liability limits.",
        "computed_at": NOW,
    },
    "landscaping": {
        "gaps": [
            {
                "line_of_business": "Pollution Liability",
                "gap_type": "missing",
                "severity": "high",
                "description": "No standalone pollution coverage. GL pollution exclusion applies. Chemical application creates drift and contamination exposure.",
                "recommendation": "Add contractors pollution liability with $1M limit. Include completed operations pollution.",
                "potential_impact": "Single herbicide drift event to organic farm neighbor could generate $500K+ claim.",
            },
            {
                "line_of_business": "Inland Marine",
                "gap_type": "inadequate_limit",
                "severity": "high",
                "description": "Equipment schedule shows $180K in coverage but actual replacement value of fleet is estimated at $280K.",
                "recommendation": "Update equipment schedule to replacement cost. Add newly acquired equipment clause.",
                "potential_impact": "Total theft loss would leave $100K gap between coverage and replacement.",
            },
            {
                "line_of_business": "Hired/Non-Owned Auto",
                "gap_type": "exclusion_risk",
                "severity": "medium",
                "description": "Employees use personal vehicles to travel to first job site. If in an accident en route, business auto policy may not respond.",
                "recommendation": "Verify hired/non-owned auto coverage is included on business auto policy.",
                "potential_impact": "Employee accident in personal vehicle on company business creates uninsured gap.",
            },
        ],
        "recommendations": [
            {
                "line_of_business": "Commercial Auto",
                "recommendation": "Add telematics discount program. Several carriers offer 10-15% premium reduction.",
                "rationale": "Fleet of trucks is the largest premium driver. Behavioral monitoring reduces claims and cost.",
                "priority": "medium",
            },
        ],
        "adequacy_score": 55,
        "summary": "Missing pollution liability is the critical gap for a company applying chemicals. Inland marine is undervalued by approximately $100K. Hired/non-owned auto coverage needs verification.",
        "computed_at": NOW,
    },
    "manufacturing": {
        "gaps": [
            {
                "line_of_business": "Cyber Liability",
                "gap_type": "inadequate_limit",
                "severity": "critical",
                "description": "Current $250K cyber limit is insufficient for CNC-connected manufacturing. Ransomware attack could halt production for weeks.",
                "recommendation": "Increase to $2M minimum. Include business interruption, system failure, and dependent business interruption.",
                "potential_impact": "Average manufacturing cyber claim is $1.6M. Current limit would cover 15% of expected loss.",
            },
            {
                "line_of_business": "Products Liability",
                "gap_type": "sublimit_concern",
                "severity": "high",
                "description": "Products/completed operations coverage shares aggregate with general liability. A single product claim could exhaust the aggregate.",
                "recommendation": "Separate products/completed operations aggregate or increase combined aggregate to $4M.",
                "potential_impact": "Defective steel component in safety-critical application could generate multi-million dollar claim.",
            },
            {
                "line_of_business": "Environmental",
                "gap_type": "missing",
                "severity": "medium",
                "description": "No environmental impairment liability. Metal fabrication generates cutting fluids, welding fumes, and scrap that require proper disposal.",
                "recommendation": "Add environmental impairment liability with $1M limit.",
                "potential_impact": "EPA cleanup order could cost $500K+ with no coverage to respond.",
            },
        ],
        "recommendations": [
            {
                "line_of_business": "Equipment Breakdown",
                "recommendation": "Add equipment breakdown with business income coverage. Current property policy has mechanical breakdown exclusion.",
                "rationale": "Single CNC machine replacement costs $250K+. Production downtime compounds the loss.",
                "priority": "high",
            },
        ],
        "adequacy_score": 48,
        "summary": "Serious coverage deficiency in cyber limits for a connected manufacturing facility. Products liability aggregate structure creates shared-limit risk. Environmental coverage is completely absent despite metal fabrication waste streams.",
        "computed_at": NOW,
    },
    "apartment_complex": {
        "gaps": [
            {
                "line_of_business": "Ordinance or Law",
                "gap_type": "missing",
                "severity": "high",
                "description": "No ordinance or law coverage. If building is damaged 50%+, code upgrade requirements could add 25-40% to rebuild cost.",
                "recommendation": "Add ordinance or law coverage with demolition, increased cost of construction, and undamaged portion coverage.",
                "potential_impact": "Code-required upgrades (ADA, fire suppression, electrical) could add $500K to rebuild cost.",
            },
            {
                "line_of_business": "Loss of Rents",
                "gap_type": "inadequate_limit",
                "severity": "medium",
                "description": "Loss of rents limited to 6 months. Major fire or water damage restoration for 48 units typically takes 12-18 months.",
                "recommendation": "Extend loss of rents to 18 months or actual loss sustained.",
                "potential_impact": "At $1.4M annual rental income, 12 additional months of lost rents = $1.4M uncovered.",
            },
            {
                "line_of_business": "Sewer/Drain Backup",
                "gap_type": "sublimit_concern",
                "severity": "medium",
                "description": "Sewer backup sublimit of $25K is far too low for a 48-unit complex. Single backup event can affect multiple units.",
                "recommendation": "Increase sewer backup sublimit to $250K minimum.",
                "potential_impact": "Multi-unit sewer backup can easily exceed $100K in remediation and tenant relocation.",
            },
        ],
        "recommendations": [
            {
                "line_of_business": "Tenant Renters Insurance",
                "recommendation": "Implement mandatory renters insurance requirement in all new leases.",
                "rationale": "Reduces property owner GL exposure and improves tenant claim recovery.",
                "priority": "high",
            },
        ],
        "adequacy_score": 60,
        "summary": "Missing ordinance or law coverage is the biggest concern for an older building. Loss of rents period is inadequate for a 48-unit restoration timeline. Sewer backup sublimit needs significant increase.",
        "computed_at": NOW,
    },
}

MOCK_STRATEGY: dict[str, dict] = {
    "restaurant": {
        "target_carriers": [
            {
                "carrier_name": "Society Insurance",
                "appetite_level": "strong",
                "rationale": "Restaurant specialist with competitive package pricing. Strong appetite for established dining establishments in PA.",
                "key_concerns": ["Loss history for past 5 years", "Liquor sales percentage of total revenue"],
            },
            {
                "carrier_name": "Erie Insurance",
                "appetite_level": "strong",
                "rationale": "PA-based carrier with regional restaurant expertise. Competitive workers comp and package programs.",
                "key_concerns": ["Employee count accuracy", "Delivery/catering operations"],
            },
            {
                "carrier_name": "Hartford",
                "appetite_level": "moderate",
                "rationale": "Strong BOP program for restaurants under $2M revenue. Good umbrella capacity.",
                "key_concerns": ["Cooking equipment age", "Franchise vs independent"],
            },
        ],
        "positioning_notes": [
            {
                "topic": "Loss History Framing",
                "framing": "Lead with the clean loss history and fire prevention investments. Position the Ansul system maintenance as proactive risk management.",
                "supporting_evidence": "Documented inspection records strengthen the submission.",
            },
            {
                "topic": "Revenue Narrative",
                "framing": "Frame the $1.8M revenue as established and stable rather than growth-stage. Show year-over-year consistency.",
                "supporting_evidence": "3-year revenue trend demonstrates operational maturity.",
            },
        ],
        "submission_summary": "Position Bella Napoli as a well-managed, established Italian restaurant with proactive risk management. Lead with clean loss history, documented fire prevention program, and stable revenue trajectory. Best markets are restaurant specialists (Society) and PA regional carriers (Erie).",
        "key_differentiators": [
            "15+ years in business demonstrates operational stability",
            "Documented fire prevention program with current Ansul inspections",
            "RAMP-certified staff for liquor service",
            "No liquor-related claims in operating history",
        ],
        "underwriter_concerns": [
            "Liquor revenue percentage -- underwriters want to see under 40% of total",
            "Delivery operations expanding insurance exposure",
            "Kitchen equipment age -- older equipment has higher fire frequency",
        ],
        "computed_at": NOW,
    },
    "landscaping": {
        "target_carriers": [
            {
                "carrier_name": "Acuity Insurance",
                "appetite_level": "strong",
                "rationale": "Strong appetite for landscaping contractors. Competitive inland marine and commercial auto programs.",
                "key_concerns": ["Tree work operations", "Snow removal exposure"],
            },
            {
                "carrier_name": "Erie Insurance",
                "appetite_level": "strong",
                "rationale": "PA regional with good contractor appetite. Package pricing with WC bundling.",
                "key_concerns": ["Fleet MVR results", "Subcontractor usage"],
            },
            {
                "carrier_name": "Employers Holdings",
                "appetite_level": "moderate",
                "rationale": "WC specialist with competitive rates for landscaping class codes. May require separate placement.",
                "key_concerns": ["EMR trending", "Class code mix"],
            },
        ],
        "positioning_notes": [
            {
                "topic": "Fleet Management",
                "framing": "Emphasize GPS tracking and maintenance program for fleet vehicles. Shows risk management maturity.",
            },
            {
                "topic": "Seasonal Revenue Mix",
                "framing": "Show year-round revenue stream if snow removal is included. Demonstrates operational diversification.",
            },
        ],
        "submission_summary": "Position GreenEdge as a professionally managed landscaping operation with fleet safety controls and diversified revenue. Target contractor-focused carriers (Acuity) and PA regionals (Erie). Separate WC placement may yield better pricing.",
        "key_differentiators": [
            "GPS tracking on all vehicles and trailers",
            "Licensed chemical applicators on staff",
            "Year-round operations with snow removal revenue",
            "No at-fault auto claims in past 3 years",
        ],
        "underwriter_concerns": [
            "Tree removal work dramatically changes risk profile and class code",
            "Trailer overnight security at job sites",
            "Chemical application creates pollution exposure excluded by standard GL",
        ],
        "computed_at": NOW,
    },
    "manufacturing": {
        "target_carriers": [
            {
                "carrier_name": "Chubb",
                "appetite_level": "strong",
                "rationale": "Strong manufacturing appetite with integrated cyber offering. Excellent products liability coverage forms.",
                "key_concerns": ["Quality control documentation", "Downstream product use"],
            },
            {
                "carrier_name": "Travelers",
                "appetite_level": "strong",
                "rationale": "Deep manufacturing expertise. Risk engineering resources add value. Competitive equipment breakdown.",
                "key_concerns": ["OSHA citation history", "Environmental compliance"],
            },
            {
                "carrier_name": "CNA",
                "appetite_level": "moderate",
                "rationale": "Manufacturing-focused underwriting team. Good package programs for mid-market manufacturers.",
                "key_concerns": ["Export operations", "Contract requirements"],
            },
        ],
        "positioning_notes": [
            {
                "topic": "Quality Control Story",
                "framing": "Lead with ISO certification and quality control procedures. Underwriters need confidence that product defects are caught before shipment.",
            },
            {
                "topic": "Cyber Posture",
                "framing": "Address CNC network segmentation proactively. Show that operational technology is separated from business IT.",
            },
        ],
        "submission_summary": "Position Precision Steel as a quality-focused manufacturer with documented processes and safety culture. Target carriers with integrated manufacturing programs (Chubb, Travelers) that can handle the cyber/products liability complexity in a single program.",
        "key_differentiators": [
            "ISO 9001 certified quality management system",
            "EMR under 1.0 demonstrates strong safety culture",
            "CNC network segmented from business IT",
            "Long-term customer contracts show revenue stability",
        ],
        "underwriter_concerns": [
            "Products used in safety-critical applications dramatically increases severity potential",
            "CNC connectivity to network creates operational technology cyber risk",
            "Environmental compliance for metal cutting fluid disposal",
        ],
        "computed_at": NOW,
    },
    "apartment_complex": {
        "target_carriers": [
            {
                "carrier_name": "Philadelphia Insurance (PHLY)",
                "appetite_level": "strong",
                "rationale": "Habitational specialist with tailored forms. Excellent loss control resources for apartment properties.",
                "key_concerns": ["Building age and renovation history", "Swimming pool/amenities"],
            },
            {
                "carrier_name": "Erie Insurance",
                "appetite_level": "strong",
                "rationale": "PA regional with competitive apartment programs. Strong relationship underwriting model.",
                "key_concerns": ["Occupancy rate", "Tenant quality indicators"],
            },
            {
                "carrier_name": "Selective Insurance",
                "appetite_level": "moderate",
                "rationale": "Good mid-market habitational appetite. Competitive property forms for newer buildings.",
                "key_concerns": ["Building code compliance", "Roof age and condition"],
            },
        ],
        "positioning_notes": [
            {
                "topic": "Property Management",
                "framing": "Highlight professional property management with documented maintenance schedules and tenant screening procedures.",
            },
            {
                "topic": "Building Improvements",
                "framing": "Emphasize recent renovations and code upgrades. Updated systems reduce both property and liability exposure.",
            },
        ],
        "submission_summary": "Position Maple Grove as a well-maintained apartment complex with professional management and consistent occupancy. Target habitational specialists (PHLY) and PA regionals (Erie). Building renovation history is key to underwriter confidence.",
        "key_differentiators": [
            "95%+ occupancy rate demonstrates desirable location and management",
            "Professional property management with 24-hour emergency maintenance",
            "Updated plumbing and electrical systems reduce water damage frequency",
            "Tenant screening with background and credit checks",
        ],
        "underwriter_concerns": [
            "Building age determines code upgrade requirements after major loss",
            "Swimming pool or amenity exposure",
            "Lead paint and asbestos potential in older construction",
        ],
        "computed_at": NOW,
    },
}

MOCK_MARKET: dict[str, dict] = {
    "restaurant": {
        "signals": [
            {
                "signal_type": "trend",
                "title": "Restaurant Insurance Market Softening",
                "description": "Restaurant insurance market showing slight softening in 2025-2026 after years of hardening. More carriers re-entering the casual dining space.",
                "relevance": "high",
                "source": "MarketScout Commercial Lines Rate Index",
            },
            {
                "signal_type": "alert",
                "title": "PA Liquor Liability Legislation",
                "description": "Pennsylvania considering amendments to dram shop liability statutes that could increase exposure for establishments.",
                "relevance": "high",
                "source": "PA General Assembly Session 2025-2026",
            },
            {
                "signal_type": "opportunity",
                "title": "Food Delivery Insurance Programs",
                "description": "New carrier programs specifically addressing third-party delivery exposure (DoorDash, UberEats). Filling a previous coverage gap.",
                "relevance": "medium",
                "source": "Industry program launches Q4 2025",
            },
        ],
        "carrier_intel": [
            {
                "carrier_name": "Society Insurance",
                "market_position": "Expanding restaurant book in Mid-Atlantic",
                "appetite_notes": "Actively seeking established restaurants with clean loss history. Competitive on package pricing.",
                "recent_changes": "New streamlined quoting for restaurants under $2.5M revenue",
            },
            {
                "carrier_name": "Erie Insurance",
                "market_position": "Stable PA market leader for small commercial",
                "appetite_notes": "Consistent restaurant appetite. Values long-term agent relationships.",
                "recent_changes": "Updated BOP forms to include basic cyber coverage",
            },
        ],
        "industry_outlook": "Restaurant sector showing recovery with stable insurance market conditions. Key watchpoints are delivery operations expansion and evolving liquor liability legislation in PA.",
        "talking_points": [
            "The restaurant insurance market is more competitive now than it has been in 3 years -- good time to market the account",
            "Society Insurance has new streamlined quoting that could accelerate placement",
            "PA liquor liability changes on the horizon make adequate limits more important than ever",
        ],
        "computed_at": NOW,
    },
    "landscaping": {
        "signals": [
            {
                "signal_type": "trend",
                "title": "Commercial Auto Rate Increases Moderating",
                "description": "Commercial auto rate increases slowing to single digits after 3 years of double-digit hikes. Better pricing environment for fleet accounts.",
                "relevance": "high",
                "source": "Council of Insurance Agents & Brokers Q4 2025",
            },
            {
                "signal_type": "risk",
                "title": "Extreme Heat Worker Safety Standards",
                "description": "OSHA finalizing heat illness prevention standard. Landscaping operations will face new compliance requirements.",
                "relevance": "high",
                "source": "OSHA proposed rulemaking 2025",
            },
            {
                "signal_type": "opportunity",
                "title": "Telematics Premium Credits Expanding",
                "description": "More carriers offering 10-20% premium credits for commercial fleet telematics programs.",
                "relevance": "medium",
                "source": "Carrier program updates 2025-2026",
            },
        ],
        "carrier_intel": [
            {
                "carrier_name": "Acuity Insurance",
                "market_position": "Growing contractor book in eastern PA",
                "appetite_notes": "Strong appetite for landscaping with clean MVRs and no tree removal. Competitive inland marine.",
                "recent_changes": "New telematics partnership offering 15% auto premium credit",
            },
        ],
        "industry_outlook": "Landscaping insurance market stabilizing after commercial auto hardening cycle. Carriers increasingly differentiating on fleet safety technology adoption. OSHA heat standards will impact operations and WC exposure.",
        "talking_points": [
            "Commercial auto rates are finally stabilizing -- strong position to negotiate renewal",
            "Telematics credits could save 15% on the auto premium, the largest line item",
            "New OSHA heat standards are coming -- proactive compliance positions this account well with underwriters",
        ],
        "computed_at": NOW,
    },
    "manufacturing": {
        "signals": [
            {
                "signal_type": "alert",
                "title": "Manufacturing Cyber Attacks Surging",
                "description": "Manufacturing overtook financial services as the most-attacked industry for the third consecutive year. Ransomware targeting OT systems specifically.",
                "relevance": "high",
                "source": "IBM X-Force Threat Intelligence Index 2025",
            },
            {
                "signal_type": "trend",
                "title": "Products Liability Severity Trending Up",
                "description": "Average products liability claim severity in manufacturing up 18% year-over-year. Nuclear verdicts impacting umbrella pricing.",
                "relevance": "high",
                "source": "Advisen Loss Data, 2025 analysis",
            },
            {
                "signal_type": "opportunity",
                "title": "Reshoring Manufacturing Incentives",
                "description": "Federal and PA state incentives for domestic manufacturing growth. Could impact revenue projections and coverage needs.",
                "relevance": "medium",
                "source": "PA Department of Community & Economic Development",
            },
        ],
        "carrier_intel": [
            {
                "carrier_name": "Chubb",
                "market_position": "Selective manufacturing appetite, focused on quality-certified operations",
                "appetite_notes": "Strong interest in ISO-certified manufacturers. Integrated cyber + property + products programs.",
                "recent_changes": "New OT-specific cyber coverage endorsement for manufacturing",
            },
            {
                "carrier_name": "Travelers",
                "market_position": "Largest commercial lines writer with deep manufacturing book",
                "appetite_notes": "Risk engineering resources for manufacturers. Values loss control partnership.",
                "recent_changes": "Updated equipment breakdown forms to include CNC-specific coverage",
            },
        ],
        "industry_outlook": "Manufacturing insurance market faces upward pressure from cyber and products liability trends. Well-managed manufacturers with documented quality and safety programs can still access competitive markets. Cyber coverage is becoming table stakes.",
        "talking_points": [
            "Cyber coverage is no longer optional for connected manufacturing -- it is a board-level risk",
            "Products liability trends make adequate limits and proper aggregate structure critical",
            "Chubb has a new OT-specific cyber endorsement that directly addresses CNC risk",
        ],
        "computed_at": NOW,
    },
    "apartment_complex": {
        "signals": [
            {
                "signal_type": "trend",
                "title": "Habitational Market Capacity Returning",
                "description": "After years of capacity constriction, more carriers re-entering the habitational space. Improved pricing environment for well-maintained properties.",
                "relevance": "high",
                "source": "AM Best Habitational Market Report 2025",
            },
            {
                "signal_type": "alert",
                "title": "PA Fair Housing Enforcement",
                "description": "Increased HUD enforcement activity in Pennsylvania for fair housing compliance. Properties should review screening procedures.",
                "relevance": "medium",
                "source": "HUD enforcement actions database 2025",
            },
            {
                "signal_type": "opportunity",
                "title": "Water Damage Mitigation Credits",
                "description": "Several carriers now offering 5-10% property premium credits for properties with water leak detection and automatic shutoff systems.",
                "relevance": "medium",
                "source": "PHLY and Selective program updates",
            },
        ],
        "carrier_intel": [
            {
                "carrier_name": "Philadelphia Insurance (PHLY)",
                "market_position": "Leading habitational specialist nationally",
                "appetite_notes": "Strong appetite for professionally managed apartments with good loss history. Best-in-class forms.",
                "recent_changes": "New water damage mitigation credit program -- 8% property premium reduction",
            },
        ],
        "industry_outlook": "Habitational market improving as capacity returns. Properties with professional management, updated systems, and strong maintenance documentation are well-positioned for competitive placement. Water damage prevention technology adoption is a key differentiator.",
        "talking_points": [
            "More carriers are writing apartments now than in the past 3 years -- good market timing",
            "Water leak detection systems could earn an 8% property credit with PHLY",
            "Fair housing compliance review should be part of the risk management conversation",
        ],
        "computed_at": NOW,
    },
}

MOCK_BRIEFS: dict[str, dict] = {
    "restaurant": {
        "industry": "Restaurant - Italian Dining",
        "things_to_confirm": [
            "When was your Ansul fire suppression system last inspected?",
            "What percentage of total revenue comes from liquor sales?",
            "Do you use any third-party delivery services?",
        ],
        "coverage_to_discuss": "Liquor liability limit is too low at $500K. PA dram shop claims regularly exceed $1M. Need to increase to $1M/$2M.",
        "underwriter_concern": "Liquor revenue percentage -- underwriters want to see under 40% of total revenue from alcohol sales.",
        "opening_talking_point": "The restaurant insurance market is more competitive now than it has been in 3 years. This is a great time to review your program and ensure your liquor liability limits match your actual exposure.",
        "risk_score": 68,
        "computed_at": NOW,
    },
    "landscaping": {
        "industry": "Landscaping - Commercial & Residential",
        "things_to_confirm": [
            "Do you perform any tree removal or stump grinding work?",
            "Where is your equipment stored overnight -- secured yard or on trailers at job sites?",
            "Do you have current pesticide applicator licenses for all chemical work?",
        ],
        "coverage_to_discuss": "No pollution liability coverage. Your chemical application work is excluded by standard GL. One herbicide drift event could be a $500K+ claim with no coverage.",
        "underwriter_concern": "Tree removal work -- if they do any, it dramatically changes the risk class and pricing.",
        "opening_talking_point": "Commercial auto rates are finally stabilizing after 3 years of increases, and there are new telematics programs that could save you 15% on your fleet premium. Let me take a look at your current program.",
        "risk_score": 62,
        "computed_at": NOW,
    },
    "manufacturing": {
        "industry": "Manufacturing - Steel Fabrication (CNC)",
        "things_to_confirm": [
            "Are your CNC machines on a separate network from your business computers?",
            "What industries use your finished steel components?",
            "What is your current experience modification rate?",
        ],
        "coverage_to_discuss": "Cyber limit at $250K is dangerously low for CNC-connected manufacturing. Average manufacturing cyber claim is $1.6M. Need to increase to $2M minimum.",
        "underwriter_concern": "Products used in safety-critical applications -- if components go into aviation, medical, or structural steel, severity potential is dramatically higher.",
        "opening_talking_point": "Manufacturing is now the most-attacked industry for cyber. With your CNC machines connected to the network, a ransomware attack could halt production entirely. Chubb just released a new cyber endorsement specifically for operational technology.",
        "risk_score": 78,
        "computed_at": NOW,
    },
    "apartment_complex": {
        "industry": "Real Estate - Apartment Complex (48 Units)",
        "things_to_confirm": [
            "What year was the building constructed, and what renovations have been done?",
            "Do you require tenants to carry renters insurance?",
            "Are there any pools, playgrounds, or fitness centers on the property?",
        ],
        "coverage_to_discuss": "No ordinance or law coverage. If you have a major fire and the building is damaged 50%+, code upgrades could add $500K to the rebuild cost with no coverage.",
        "underwriter_concern": "Building age -- older buildings face code upgrade requirements that can add 25-40% to reconstruction costs after a major loss.",
        "opening_talking_point": "More carriers are writing apartments now than in the past 3 years, so the market is favorable. PHLY has a new water damage prevention credit that could save you 8% on your property premium if you install leak detection.",
        "risk_score": 58,
        "computed_at": NOW,
    },
}
