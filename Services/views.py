from django.shortcuts import render

# Create your views here.

Services = [
    {
        'slug':'programming',
        'title': 'programming',
        'image': '2.jpg',
        'content': 'The architect takes notes of what the owner states that they want in the project Usually, the architect provides these notes in some form of typed format, possibly with photos of the property, with some discussion of site features and opportunities for the to-be-built items.  The architect will often include a site visit with a typed understanding of site elements and how and where the built structures might be located.'
    },
{
        'slug':'Schematic Design',
        'title': 'Schematic Design',
        'image': '2.jpg',
        'content':'The architect uses the Program established in the previous phase of work to conceptually create a diagram or plans of the proposed project.In SFR projects, some architects may combine Design Development with Schematic Design,as sometimes some architects only make a hazy sketch, in schematics, while othersstart out the project on computer and stay on computer, as they feel that is a moreefficient method and that nothing is wasted.  However, there is no precise right or wrong method.Each architect has their own preferences about how they go about creating something from nothing.Some architects produce only floor plans and site plans at this stage, often for SFR projects.'
},
{
        'slug':'Design Development',
        'title': 'Design Development',
        'image': '3.png',
        'content': 'This is where additional detail is added to the previous Schematic Design.Some architects add exterior building elevations at this point and perhaps a roof plan.  Others may decide to include a building section.  However, there is no specific right or wrong method.  Whatever works for each firm.  Additional dimensions are tested to insure that various items will fit into the proposed design.  And additional dimensions are added to the work.'
},
{
        'slug':'Construction Documents',
        'title': 'Construction Documents',
        'image': '4.jpg',
        'content':'Traditionally, this = Working Drawings & Specifications. This is where the final details are added to the project.  Building sections, wall sections, finish schedules, door schedules, title sheets, index sheets, final graphics, blow-up detail plans and elevations of critical conditions, notes, final detailed dimensions, interior elevations (depending on scope of services and other additional services).  The architect does coordinate all the building consultants, whether provided under the architect’s umbrella or not. The amount of fee can and will affect the amount of drawings and other items provided by the architect.'
},
{
        'slug':'Construction Administration',
        'title': 'Construction Administration',
        'image': '5.jpg',
        'content':'These services are Not required by law.  These complex additional services are where the architect periodically visits the project site, reviews contractor submittals, including shop drawings for the various items of the project, including but not limited to doors & windows, insulation, concrete, wood, paint, and many other items.  Without the architect’s watchful eye, any of these items could be changed by the contractor and suppliers without the owner’s knowledge, cheapening the project, damaging its durability, increasing its monthly utility charges and possibly leaking, rotting and being compromised structurally.Furthermore, during construction, if the architect is compensated to do so, they can process the contractor’s pay requests, checking on the progress of the construction and comparing that with the amount invoiced.  Without this knowledgeable service, owners overpay up-front, which can induce a builder to walk off the job later, after they have obtained too much money too quickly, leaving the owner stuck with a project that will cost more to complete than remains in the budget.  Very few owners have this type of experience in-house and would do well to pay their architect to help them. And there many other activities during construction that are too numerous to mention here.  Serious situations that arise and without the architect’s wise and helping hands, projects can develop all sorts of problems that can have them come screeching to a halt.'
},
{
        'slug':'Project Management',
        'title': 'Project Management',
        'image': '6.jpg',
        'content':'This is a catch-all for anything and everything that the owner can’t handle but needs to be managed for them, not included in any other service.  For instance: selection of colors, tile, paint, appliances, coordinating a home-owners association and other situations that can and will develop.  It is wise to have the architect on-call for such things on an hourly basis.'
},
{
        'slug':'3D Imagery',
        'title': '3D Imagery',
        'image': '7.jpeg',
        'content':'Architects may offer three-dimensional hand-drawn or computerized imagery of their designs.  This can also involve 3D animations, which is a movie of a Client’s project.  Images can be either fixed (static) of a single viewpoint, or have multiple single views.  The imagery may be plain and only consist of lines, or may be near-photo-realistic.  Architects typically will not include such imagery in their Basic Services, unless paid additionally for these services.  3D computerized imagery may be provided to the Architect from a third party specialty source, as such imagery typically requires expensive and complex software and powerful computers to provide high-quality images. Architects may provide these services as a fixed price or hourly.'
}

]


def OurService(request):
    return render(request,'Services/Services.html',{'Services':Services})


def Service_details(request,slug):
    Service=next(Service for Service in Services if Service['slug']==slug)
    return render(request,'Services/Services_details.html',{'Service':Service})


