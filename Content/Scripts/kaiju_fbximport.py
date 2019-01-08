######################## FBX #########################
import os.path
from unreal_engine.classes import PyFbxFactory

# instantiate a new factory
fbx_factory = PyFbxFactory()

# build path
kaiju_assets_dir = os.path.join(os.path.expanduser('~/Desktop'),'Kaiju_Assets/Slicer')


slicer_fbx = os.path.join(kaiju_assets_dir, 'slicer.fbx')


# configure the factory
fbx_factory.ImportUI.bCreatePhysicsAsset = False
fbx_factory.ImportUI.bImportMaterials = False
fbx_factory.ImportUI.bImportTextures = False 
fbx_factory.ImportUI.bImportAnimations = False

fbx_factory.ImportUI.SkeletalMeshImportData.ImportUniformScale = 0.1;

#import mesh
slicer_mesh = fbx_factory.factory_import_object(slicer_fbx, '/Game/Kaiju/Slicer')


######################## Material #########################
from unreal_engine.classes import MaterialFactoryNew

material_factory = MaterialFactoryNew()

material_blades = material_factory.factory_create_new('/Game/Kaiju/Slicer/Blades_Material')
material_body = material_factory.factory_create_new('/Game/Kaiju/Slicer/Body_Material')


######################## Texture #########################
from unreal_engine.classes import TextureFactory

# instant factory
texture_factory = TextureFactory()

# overwritten
texture_factory.OverwriteYesorNoToAllState = 2

slicer_blade_texture_base_color_tga = os.path.join(kaiju_assets_dir, 'Textures/slicer_blade_BaseColor.tga')
slicer_blade_texture_base_color = texture_factory.factory_import_object(slicer_blade_texture_base_color_tga,'/Game/Kaiju/Slicer/Textures')

slicer_blade_texture_normal_tga = os.path.join(kaiju_assets_dir, 'Textures/slicer_blade_Normal.tga')
slicer_blade_texture_normal = texture_factory.factory_import_object(slicer_blade_texture_normal_tga,'/Game/Kaiju/Slicer/Textures')

slicer_blade_texture_emissive_tga = os.path.join(kaiju_assets_dir, 'Textures/slicer_blade_Emissive.tga')
slicer_blade_texture_emissive = texture_factory.factory_import_object(slicer_blade_texture_emissive_tga,'/Game/Kaiju/Slicer/Textures')

# orm stands for occlusionRoughnessMetallic
slicer_blade_texture_orm_tga = os.path.join(kaiju_assets_dir,'Textures/slicer_blade_OcclusionRoughnessMetallic.tga')
slicer_blade_texture_orm = texture_factory.factory_import_object(slicer_blade_texture_orm_tga, '/Game/Kaiju/Slicer/Textures')

slicer_texture_base_color_tga = os.path.join(kaiju_assets_dir,'Textures/slicer_BaseColor.tga')
slicer_texture_base_color = texture_factory.factory_import_object(slicer_texture_base_color_tga, '/Game/Kaiju/Slicer/Textures')

slicer_texture_normal_tga = os.path.join(kaiju_assets_dir,'Textures/slicer_Normal.tga')
slicer_texture_normal = texture_factory.factory_import_object(slicer_texture_normal_tga, '/Game/Kaiju/Slicer/Textures')

slicer_texture_emissive_tga = os.path.join(kaiju_assets_dir,'Textures/slicer_Emissive.tga')
slicer_texture_emissive = texture_factory.factory_import_object(slicer_texture_emissive_tga, '/Game/Kaiju/Slicer/Textures')

# orm stands for occlusionRoughnessMetallic
slicer_texture_orm_tga = os.path.join(kaiju_assets_dir,'Textures/slicer_OcclusionRoughnessMetallic.tga')
slicer_texture_orm = texture_factory.factory_import_object(slicer_texture_orm_tga, '/Game/Kaiju/Slicer/Textures')

######################## Setup Material blade #########################

# turn sRGB off for orm textures
slicer_blade_texture_orm.SRGB = False

from unreal_engine.classes import MaterialExpressionTextureSample
from unreal_engine.enums import EMaterialSamplerType
from unreal_engine.structs import colorMaterialInput, VectorMaterialInput, ScalarMaterialInput

# notify editor modify the material
material_blades.modify()

# create basecolor node
material_blades_base_color = MaterialExpressionTextureSample('', material_blades)
material_blades_base_color.Texture = slicer_blade_texture_base_color
material_blades_base_color.MaterialExpressionEditorX = -400
material_blades_base_color.MaterialExpressionEditorY = 0

# create normal node
material_blades_normal = MaterialExpressionTextureSample('',material_blades)
material_blades_normal.Texture = slicer_blade_texture_normal
# force the sampler to 'Normal'
material_blades_normal.SamplerType = EMaterialSamplerType.SAMPLERTYPE_Normal
material_blades_normal.MaterialExpressionEditorX = -400
material_blades_normal.MaterialExpressionEditorY = 200

# create emissive node
material_blades_emissive = MaterialExpressionTextureSample('', material_blades)
material_blades_emissive.Texture = slicer_blade_texture_emissive
material_blades_emissive.MaterialExpressionEditorX = -400
material_blades_emissive.MaterialExpressionEditorY = 400

# create ORM
material_blades_orm = MaterialExpressionTextureSample('', material_blades)
material_blades_orm.Texture = slicer_blade_texture_orm
# force the sampler to 'LinearColor' (remember you turned off sRGB)
material_blades_orm.SamplerType = EMaterialSamplerType.SAMPLERTYPE_LinearColor
material_blades_orm.MaterialExpressionEditorX = -400
material_blades_orm.MaterialExpressionEditorY = 600

# assign nodes
material_blades.Expressions = [material_blades_base_color, material_blades_normal, material_blades_emissive, material_blades_orm]

# link nodes
material_blades.BaseColor = colorMaterialInput(Expression=material_blades_base_color)
# normal are vectors
material_blades.Normal = VectorMaterialInput(Expression=material_blades_normal)
material_blades.EmissiveColor = colorMaterialInput(Expression=material_blades_emissive)
# use mask
material_blades.Roughness=ScalarMaterialInput(expression=material_blades_orm, Mask=1, MaskG=1)
material_blades.Metallic=ScalarMaterialInput(expression=material_blades_orm, Mask=1, MaskB=1)
material_blades.AmbientOcclusion=ScalarMaterialInput(expression=material_blades_orm, Mask=1, MaskR=1)

# run material 
material_blades.post_edit_change()


######################## Setup Material Body #########################
from unreal_engine.classes import MaterialExpressionSine, MaterialExpressionMultiply, MaterialExpressionTime
from unreal_engine.structs import ExpressionInput

# turn sRGB off
slicer_texture_orm.SRGB = False 

material_body.modify()

material_body_base_color = MaterialExpressionTextureSample('', material_body)
material_body_base_color.Texture = slicer_texture_base_color
material_body_base_color.MaterialExpressionEditorX = -400
material_body_base_color.MaterialExpressionEditorY = 0

material_body_normal = MaterialExpressionTextureSample('', material_body)
material_body_normal.Texture = slicer_texture_normal
material_body_normal.SamplerType = EMaterialSamplerType.SAMPLERTYPE_Normal
material_body_normal.MaterialExpressionEditorX = -400
material_body_normal.MaterialExpressionEditorY = 200

material_body_emissive = MaterialExpressionTextureSample('', material_body)
material_body_emissive.Texture = slicer_texture_emissive
material_body_emissive.MaterialExpressionEditorX = -400
material_body_emissive.MaterialExpressionEditorY = 400

material_body_orm = MaterialExpressionTextureSample('', material_body)
material_body_orm.Texture = slicer_texture_orm
material_body_orm.SamplerType = EMaterialSamplerType.SAMPLERTYPE_LinearColor
material_body_orm.MaterialExpressionEditorX = -400
material_body_orm.MaterialExpressionEditorY = 600

# create a sine node
material_body_sine = MaterialExpressionSine('', material_body)
material_body_sine.MaterialExpressionEditorX = -1000
material_body_sine.MaterialExpressionEditorY = 0

# create a time node
material_body_time = MaterialExpressionTime('', material_body)
material_body_time.MaterialExpressionEditorX = -1200
material_body_time.MaterialExpressionEditorY = 0

# create mutiply node
material_body_multiply = MaterialExpressionMultiply('', material_body)
material_body_multiply.MaterialExpressionEditorX = -800
material_body_multiply.MaterialExpressionEditorY = 0

# assign node to graph
material_body.Expressions = [material_body_base_color, material_body_normal, material_body_orm, material_body_emissive, material_body_sine, material_body_multiply, material_body_time ]

# connect node
material_body_sine.Input = ExpressionInput(Expression=material_body_time)
material_body_multiply.A = ExpressionInput(Expression=material_body_emissive)
material_body_multiply.B = ExpressionInput(Expression=material_body_sine)

# link node
material_body.BaseColor = colorMaterialInput(Expression=material_body_base_color)
material_body.EmissiveColor = colorMaterialInput(Expression=material_body_multiply)
material_body.Normal = VectorMaterialInput(Expression=material_body_normal)
material_body.Roughness = ScalarMaterialInput(Expression=material_body_orm, Mask=1, MaskG=1)
material_body.Metallic = ScalarMaterialInput(Expression=material_body_orm, Mask=1, MaskB=1)
material_body.AmbientOcclusion = ScalarMaterialInput(Expression=material_body_orm, Mask=1, MaskR=1)

# run material comilation
material_body.post_edit_change()

from unreal_engine.structs import SkeletalMaterial, MeshUVChannelInfo

# SkeletalMaterial is a struct holding information about material mappings
# the Materials property is the array of assigned materials (setting UVChannelData is required, otherwise you will get assertions)
slicer_mesh.Materials = [SkeletalMaterial(MaterialInterface=material_blades, MaterialSlotName='Blades', UVChannelData=MeshUVChannelInfo(bInitialized=True)),SkeletalMaterial(MaterialInterface=material_body, MaterialSlotName='Body', UVChannelData=MeshUVChannelInfo(bInitialized=True))]


# save them all
slicer_mesh.save_package()
material_blades.save_package()
material_body.save_package()

# animation import

anim_factory = PyFbxFactory()
anim_factory.ImportUI.Skeleton = slicer_mesh.Skeleton
anim_factory.ImportUI.bImportMesh = False 
anim_factory.ImportUI.bImportMaterials = False
anim_factory.ImportUI.bImportTextures = False  

anim_factory.ImportUI.AnimSequenceImportData.ImportUniformScale = 0.1

slicer_idle_fbx = os.path.join(kaiju_assets_dir, 'Animations/slicer_idle.fbx')
animation_idle = anim_factory.factory_import_object(slicer_idle_fbx, '/Game/Kaiju/Slicer/Animations')

slicer_bored_fbx = os.path.join(kaiju_assets_dir, 'Animations/slicer_bored.fbx')
animation_bored = anim_factory.factory_import_object(slicer_bored_fbx, '/Game/Kaiju/Slicer/Animations')

slicer_attack_fbx = os.path.join(kaiju_assets_dir, 'Animations/slicer_attack.fbx')
animation_attack = anim_factory.factory_import_object(slicer_attack_fbx, '/Game/Kaiju/Slicer/Animations')

slicer_roaring_fbx = os.path.join(kaiju_assets_dir, 'Animations/slicer_roaring.fbx')
animation_roaring = anim_factory.factory_import_object(slicer_roaring_fbx, '/Game/Kaiju/Slicer/Animations')

slicer_run_fbx = os.path.join(kaiju_assets_dir, 'Animations/slicer_run.fbx')
animation_run = anim_factory.factory_import_object(slicer_run_fbx, '/Game/Kaiju/Slicer/Animations')

slicer_walk_fbx = os.path.join(kaiju_assets_dir, 'Animations/slicer_walk.fbx')
animation_walk = anim_factory.factory_import_object(slicer_walk_fbx, '/Game/Kaiju/Slicer/Animations')


# create BlendSpace1D

from unreal_engine.classes import BlendSpaceFactory1D
from unreal_engine.structs import BlendSample, BlendParameter 
from unreal_engine import FVector
import unreal_engine as ue


blend_space_factory=BlendSpaceFactory1D()
blend_space_factory.TargetSkeleton = slicer_mesh.Skeleton

# create the asset
slicer_locomotion = blend_space_factory.factory_create_new('/Game/Kaiju/Slicer/Animations/slicer_locomotion')

ue.open_editor_for_asset(slicer_locomotion)

# set blend parameters
slicer_locomotion.modify()
slicer_locomotion.BlendParameters = BlendParameter(DisplayName='Speed', Min=0, Max=300, GridNum=2)

# assign animations
# 0 -> idle
# 150 -> walk
# 300 -> run
# mark them as 'valid' explicitely !
slicer_locomotion.SampleData = [BlendSample(Animation=animation_idle, SampleValue=FVector(0,0,0), bIsValid=True, RateScale=1), BlendSample(Animation=animation_walk, SampleValue=FVector(150,0,0), bIsValid=True, RateScale=1), BlendSample(Animation=animation_run, SampleValue=FVector(300,0,0), bIsValid=True, RateScale=1)]

slicer_locomotion.post_edit_change()

slicer_locomotion.save_package()
ue.close_editor_for_asset(slicer_locomotion)


# create animation BP
from unreal_engine.classes import AnimBlueprintFactory 

anim_bp = ue.find_asset('/Game/Kaiju/Slicer/slicer_AnimBP.slicer_AnimBP')
if anim_bp:
	ue.delete_asset(anim_bp.get_path_name())

anim_bp_factory = AnimBlueprintFactory()
anim_bp_factory.TargetSkeleton = slicer_mesh.Skeleton

anim_bp = anim_bp_factory.factory_create_new('/Game/Kaiju/Slicer/slicer_AnimBP')


# DoAttack custom event
node_do_attack = anim_bp.UbergraphPages[0].graph_add_node_custom_event('DoAttack', 0, -200)

# Boring custom event
node_boring = anim_bp.UbergraphPages[0].graph_add_node_custom_event('Boring', 0, -400)

# bool variables
ue.blueprint_add_member_variable(anim_bp, 'Attack', 'bool')
ue.blueprint_add_member_variable(anim_bp, 'Bored', 'bool')

# float variable
ue.blueprint_add_member_variable(anim_bp, 'Speed', 'float')

# add node 
from unreal_engine.classes import KismetSystemLibrary, KismetMathLibrary

# set attack
node_set_attack001 = anim_bp.UbergraphPages[0].graph_add_node_variable_set('Attack', None, 300, -200)
node_set_attack001.node_find_pin('Attack').default_value = 'true'

# delay
node_delay_2_seconds = anim_bp.UberGraphPages[0].graph_add_node_call_function(KismetSystemLibrary.Delay, 600, -200)
node_delay_2_seconds.node_find_pin('Duration').default_value = '2.0'

# set attack to false
node_set_attack002 = anim_bp.UbergraphPages[0].graph_add_node_variable_set('Attack', None, 900, -200)
node_set_attack002.node_find_pin('Attack').default_value = 'false'

# add bored
node_set_bored001 = anim_bp.UbergraphPages[0].graph_add_node_variable_set('Bored', None, 300, -400)
node_set_bored001.node_find_pin('Bored').default_value = 'true'

# delay
node_delay_5_seconds = anim_bp.UberGraphPages[0].graph_add_node_call_function(KismetSystemLibrary.Delay, 600, -400)
node_delay_5_seconds.node_find_pin('Duration').default_value = '5.0'

# add bored
node_set_bored002 = anim_bp.UbergraphPages[0].graph_add_node_variable_set('Bored', None, 900, -400)
node_set_bored002.node_find_pin('Bored').default_value = 'false'


# link nodes

node_do_attack.node_find_pin('then').make_link_to(node_set_attack001.node_find_pin('execute'))
node_set_attack001.node_find_pin('then').make_link_to(node_delay_2_seconds.node_find_pin('execute'))
node_delay_2_seconds.node_find_pin('then').make_link_to(node_set_attack002.node_find_pin('execute'))

node_boring.node_find_pin('then').make_link_to(node_set_bored001.node_find_pin('execute'))
node_set_bored001.node_find_pin('then').make_link_to(node_delay_5_seconds.node_find_pin('execute'))
node_delay_5_seconds.node_find_pin('then').make_link_to(node_set_bored002.node_find_pin('execute'))


# speed 
from unreal_engine.classes import K2Node_Event, K2Node_CallFunction, Actor, AnimInstance

def find_event_node(graph, name):
	for node in graph.Nodes:
		if node.is_a(K2Node_Event):
			if node.EventReference.MemberName == name:
				return node
	return None 

def find_function_node(graph, name):
	for node in graph.Nodes:
		if node.is_a(K2Node_CallFunction):
			if node.FunctionReference.MemberName == name:
				return node 
	return None 

update_animation_event = find_event_node(anim_bp.UberGraphPages[0], 'BlueprintUpdateAnimation')
try_get_pawn_owner = find_function_node(anim_bp.UberGraphPages[0], 'TryGetPawnOwner')

if not try_get_pawn_owner:
	try_get_pawn_owner = anim_bp.UbergraphPages[0].graph_add_node_call_function(AnimInstance.TryGetPawnOwner, 0, 200)
	ue.log('***************** Re Assign PawnOwner *****************')


# create velocity, vectorlength node 
node_get_velocity = anim_bp.UbergraphPages[0].graph_add_node_call_function(Actor.GetVelocity, 300, 200)
node_vector_length = anim_bp.UbergraphPages[0].graph_add_node_call_function(KismetMathLibrary.VSize, 600, 200)
node_speed_set = anim_bp.UbergraphPages[0].graph_add_node_variable_set('Speed', None, 900, 0)

# link nodes
update_animation_event.node_find_pin('then').make_link_to(node_speed_set.node_find_pin('execute'))
try_get_pawn_owner.node_find_pin('ReturnValue').make_link_to(node_get_velocity.node_find_pin('self'))
node_get_velocity.node_find_pin('ReturnValue').make_link_to(node_vector_length.node_find_pin('A'))
node_vector_length.node_find_pin('ReturnValue').make_link_to(node_speed_set.node_find_pin('Speed'))




from unreal_engine.classes import AnimGraphNode_StateMachine

# Create State Machine
state_machine = anim_bp.FunctionGraphs[0].graph_add_node(AnimGraphNode_StateMachine, -300, 0)
state_machine.EditorStateMachineGraph.set_name('Slicer State Machine')

# connect nodes
state_machine.node_find_pin('Pose').make_link_to(anim_bp.FunctionGraphs[0].Nodes[0].node_find_pin('Result'))

# adding state
from unreal_engine.classes import AnimStateNode

# locomotion
locomotion_state = state_machine.EditorStateMachineGraph.graph_add_node(AnimStateNode, 200, 0)
locomotion_state.BoundGraph.set_name('Locomotion')

# attack
attack_state = state_machine.EditorStateMachineGraph.graph_add_node(AnimStateNode, 400, -150)
attack_state.BoundGraph.set_name('Attack')

# Bored
bored_state = state_machine.EditorStateMachineGraph.graph_add_node(AnimStateNode, 400, 150)
bored_state.BoundGraph.set_name('Bored')

# Bored state -> simply play an animation
from unreal_engine.classes import AnimGraphNode_SequencePlayer
from unreal_engine.structs import AnimNode_SequencePlayer

bored_player = bored_state.BoundGraph.graph_add_node(AnimGraphNode_SequencePlayer, -300, 0)
bored_player.Node = AnimNode_SequencePlayer(Sequence=animation_bored, bLoopAnimation=True)
bored_player.node_find_pin('Pose').make_link_to(bored_state.BoundGraph.Nodes[0].node_find_pin('Result'))

# Locomotion State -> speed

from unreal_engine.classes import AnimGraphNode_BlendSpacePlayer
from unreal_engine.structs import AnimNode_BlendSpacePlayer

locomotion_plyer = locomotion_state.BoundGraph.graph_add_node(AnimGraphNode_BlendSpacePlayer, -300, 0)