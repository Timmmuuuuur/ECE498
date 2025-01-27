import 'dart:math';

import 'package:campusalert/schemas/roomnode.dart';
import 'package:campusalert/services/a_star.dart';
import 'package:latlong2/latlong.dart';

class RoomGraph extends Graph<RoomNode> {
  late Iterable<RoomNode> _allNodes;
  late Set<RoomNode> _allExits;
  late AStar<RoomNode> astar;
  final Distance distance = Distance();

  RoomGraph._();

  static Future<RoomGraph> create() async {
    var inst = RoomGraph._();
    inst._allNodes = await RoomNode.allNodes;
    inst._allExits = await RoomNode.allExits;
    inst.astar = AStar(inst);
    return inst;
  }

  @override
  Iterable<RoomNode> get allNodes => _allNodes;

  @override
  num getDistance(RoomNode a, RoomNode b) => distance(
        a.latlong.toLatLng(),
        b.latlong.toLatLng(),
      );

  @override
  num getHeuristicDistance(RoomNode a, Set<RoomNode> goals) => goals
      .map((g) => distance(
            a.latlong.toLatLng(),
            g.latlong.toLatLng(),
          ))
      .reduce((val, el) => min(val, el));

  @override
  Future<Iterable<RoomNode>> getNeighboursOf(RoomNode node) {
    return node.neighbours;
  }

  Future<List<RoomNode>> getRoute(RoomNode start) async {
    return (await astar.findPath(start, _allExits)).toList();
  }
}
