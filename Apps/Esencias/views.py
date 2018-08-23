from django.urls import reverse
from django.shortcuts import render
from django.db.models import Q
from .forms import AltaPaciente, NuevaConsulta
from django.http import HttpResponseRedirect
from Apps.Esencias.models import Esencia, Sintoma, Subsintoma, Formula, Paciente, Consulta


# Create your views here.

def esencias(request, id=''):
    esencias = Esencia.objects.filter(Sets__contains=id).order_by("Nombre")
    contexto = {'esencias': esencias}

    return render(request, 'Esencias/esencias.html', contexto)


def sintomas(request):
    sintomas = Sintoma.objects.filter(id__gte=1).order_by('Sintoma')
    contexto = {'sintomas': sintomas}

    return render(request, 'Esencias/sintomas.html', contexto)


def subsintomas(request, id):
    sintoma = Sintoma.objects.get(id=id)
    subsintomas = Subsintoma.objects.filter(Sintoma_id=id).order_by('Subsintoma')
    esencias = Esencia.objects.all()
    formulas = Formula.objects.all()
    contexto = {'subsintomas': subsintomas, 'esencias': esencias, 'sintoma': sintoma, 'formulas': formulas}
    return render(request, 'Esencias/subsintomas.html', contexto)


def esenciadesc(request, id, sintoma='0', formula='0', string='0', superformula='0'):
    formula = Formula.objects.get(id=formula)
    sintoma = Sintoma.objects.get(id=sintoma)
    esencia = Esencia.objects.get(id=id)
    superformulas = Formula.objects.get(id=superformula)
    contexto = {'esencia': esencia, 'sintoma': sintoma, 'formula': formula, 'string': string, 'superformulas': superformulas}

    return render(request, 'Esencias/esenciadesc.html', contexto)


def formulas(request):
    formulas = Formula.objects.filter(id__gte=1,Personalizada='N').order_by('Nombre')
    contexto = {'formulas': formulas}

    return render(request, 'Esencias/formulas.html', contexto)


def formula(request, id, sintoma='0', string='0', superformula='0'):
    formula = Formula.objects.get(id=id)
    sintoma = Sintoma.objects.get(id=sintoma)
    esencias = formula.Esencia.all()
    subformulas = formula.SubFormula.all()
    superformulas = Formula.objects.get(id=superformula)
    contexto = {'formula': formula, 'esencias': esencias, 'sintoma': sintoma, 'string': string, 'subformulas': subformulas, 'superformulas':superformulas}

    return render(request, 'Esencias/formula.html', contexto)



def search(request):
    if request.method == 'GET':
        string = request.GET.get('b', None)
        formulas = Formula.objects.filter((Q(Nombre__contains=string) | Q(Subtitulo__contains=string) | Q(Positivos__contains=string) | Q( Negativos__contains=string) | Q( Descripcion__contains=string) | Q( TestIntuitivo__contains=string)), id__gte=1)
        esencias = Esencia.objects.filter(Q(Nombre__contains=string) | Q(Subtitulo__contains=string) | Q(Positivos__contains=string) | Q( Negativos__contains=string) | Q( Descripcion__contains=string) | Q( TestIntuitivo__contains=string))
        contexto = {'esencias': esencias, 'formulas': formulas, 'string': string}

        return render(request, 'Esencias/search.html', contexto)

def fisicos(request):
    fisicos = Formula.objects.filter(id__gte=1,Personalizada='S').order_by('id')
    contexto = {'fisicos': fisicos}

    return render(request, 'Esencias/fisicos.html', contexto)

def fisico(request, id):
    formula = Formula.objects.get(id=id)
    esencias = formula.Esencia.all()
    subformulas = formula.SubFormula.all()
    contexto = {'formula': formula, 'esencias': esencias, 'subformulas': subformulas}

    return render(request, 'Esencias/fisico.html', contexto)

def add(request):
    if request.method == 'POST':

        form = AltaPaciente(request.POST)

        if form.is_valid():

            formu = Paciente.objects.create(
                Nombre=form.cleaned_data['Nombre'],
                Apellido=form.cleaned_data['Apellido'],
                FechaNacimiento=form.cleaned_data['FechaNacimiento'],
                HoraNacimiento=form.cleaned_data['HoraNacimiento'],
                LugarNacimiento=form.cleaned_data['LugarNacimiento'],
                Sexo=form.cleaned_data['Sexo'],
                Direccion=form.cleaned_data['Direccion'],
                Telefono=form.cleaned_data['Telefono'],
                Localidad=form.cleaned_data['Localidad'],
                Email=form.cleaned_data['Email'],
                Recomendado=form.cleaned_data['Profesion'],
                Psicologo=form.cleaned_data['Psicologo'],
                Profesion=form.cleaned_data['Profesion'],
                Pareja=form.cleaned_data['Pareja'],
                ParejaTiempo=form.cleaned_data['ParejaTiempo'],
                Hijos=form.cleaned_data['Hijos'],
                Constelaciones=form.cleaned_data['Constelaciones'],
                Yoga=form.cleaned_data['Yoga'],
                OtrosSistemas=form.cleaned_data['OtrosSistemas'],
                DetalleSistemas=form.cleaned_data['DetalleSistemas'],
                Operaciones=form.cleaned_data['Operaciones'],
                Anemia=form.cleaned_data['Anemia'],
                Diabetes=form.cleaned_data['Diabetes'],
                Medicacion=form.cleaned_data['Medicacion'],
                EnfermedadesPasadas=form.cleaned_data['EnfermedadesPasadas'],
                EnfermedadesActuales=form.cleaned_data['EnfermedadesActuales'],
                Alimentacion=form.cleaned_data['Alimentacion'],
                AntecFamilMental=form.cleaned_data['AntecFamilMental'],
                Abortos=form.cleaned_data['Abortos'],
                Hermanos=form.cleaned_data['Hermanos'],
                MotivoVisita=form.cleaned_data['MotivoVisita'],
                Observaciones=form.cleaned_data['Observaciones'],
            )
            formu.save()

            return HttpResponseRedirect('/paciente/' + str(formu.id))
    else:
        form = AltaPaciente()

    return render(request, 'pacientes/add.html', {'form': form})

def nuevaconsulta(request,id):
    if request.method == 'POST':

        form = NuevaConsulta(request.POST)

        if form.is_valid():

            Consulta.objects.create(
                Paciente=Paciente.objects.get(id=id),
                Observaciones=form.cleaned_data['Observaciones'],
                Receta=form.cleaned_data['Receta'],
            ).save()

            return HttpResponseRedirect('/esencias')
    else:
        form = NuevaConsulta()

    return render(request, 'pacientes/nuevaconsulta.html', {'form': form})


def paciente(request, id):
    paciente = Paciente.objects.get(id=id)
    contexto = {'paciente': paciente}


    return render(request, 'pacientes/view.html', contexto)
